from pyrogram import Client, filters
from pyrogram.types import Message
import time

import psutil
import shutil

@Client.on_message(filters.command("usage"))
async def usage_cmd(client, message):
    """Handles the /usage command to display system resource usage."""
    reply = await message.reply("`Extracting all Usage!!`")

    total, used, free = shutil.disk_usage("/")
    total_gb = total / (1024**3)
    used_gb = used / (1024**3)
    free_gb = free / (1024**3)

    ram = psutil.virtual_memory()
    total_ram = ram.total / (1024**3)
    used_ram = ram.used / (1024**3)
    free_ram = ram.available / (1024**3)
    ram_percent = ram.percent

    swap = psutil.swap_memory()
    total_swap = swap.total / (1024**3)
    used_swap = swap.used / (1024**3)
    free_swap = swap.free / (1024**3)
    swap_percent = swap.percent

    cpu_usage = psutil.cpu_percent(interval=1)

    # Handle network stats safely
    try:
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent / (1024**2)
        bytes_recv = net_io.bytes_recv / (1024**2)
        net_msg = (
            f"**📡 Network Usage:**\n"
            f"• **Uploaded:** `{bytes_sent:.2f} MB`\n"
            f"• **Downloaded:** `{bytes_recv:.2f} MB`\n\n"
        )
    except PermissionError:
        net_msg = "**📡 Network Usage:** `Not available on PRoot`\n\n"

    # Bot process usage
    process = psutil.Process()
    bot_cpu_usage = process.cpu_percent(interval=1)
    bot_memory_usage = process.memory_info().rss / (1024**2)

    # Final message construction
    msg = (
        f"<blockquote>**📊 System Usage Stats:**</blockquote>\n\n"
        f"**💾 Disk Usage:**\n"
        f"• **Total:** `{total_gb:.2f} GB`\n"
        f"• **Used:** `{used_gb:.2f} GB`\n"
        f"• **Free:** `{free_gb:.2f} GB`\n\n"
        f"**🖥 RAM Usage:**\n"
        f"• **Total:** `{total_ram:.2f} GB`\n"
        f"• **Used:** `{used_ram:.2f} GB` ({ram_percent}%)\n"
        f"• **Free:** `{free_ram:.2f} GB`\n\n"
        f"**🔄 Swap Usage:**\n"
        f"• **Total:** `{total_swap:.2f} GB`\n"
        f"• **Used:** `{used_swap:.2f} GB` ({swap_percent}%)\n"
        f"• **Free:** `{free_swap:.2f} GB`\n\n"
        f"**⚡ CPU Usage:** `{cpu_usage:.2f}%`\n\n"
        f"{net_msg}"
        f"**🤖 Bot Resource Usage:**\n"
        f"• **CPU:** `{bot_cpu_usage:.2f}%`\n"
        f"• **Memory:** `{bot_memory_usage:.2f} MB`"
    )

    await reply.edit_text(msg)

@Client.on_callback_query(filters.regex("^add_admin$") & filters.private)
async def add_new_admins(client, query):
    if not query.from_user.id in client.admins:
        return await client.send_message(query.from_user.id, client.reply_text)
    
    if len(ids) == 0:
        return await message.reply("Send user ids along with that command!\nEg: `/add_admin 838278682 83622928 82789928`")
    try:
        for identifier in ids:
            if int(identifier) not in client.admins:
                client.admins.append(int(identifier))
    except Exception as e:
        return await message.reply(f"Error: {e}")
    return await message.reply(f"{len(ids)} admin {'id' if len(ids)==1 else 'ids'} have been promoted!!\n\nSend /rm_admin to remove any id and /admins to check admin list.")

@Client.on_message(filters.command("rm_admin") & filters.private)
async def add_new_admins(client, message):
    if not message.from_user.id in client.admins:
        return await message.reply(client.reply_text)
    ids = message.text.split()[1:]
    if len(ids) == 0:
        return await message.reply("Send user ids along with that command!\nEg: `/rm_admin 838278682 83622928 82789928`")
    try:
        for identifier in ids:
            if int(identifier) not in client.admins:
                client.admins.remove(int(identifier))
    except Exception as e:
        return await message.reply(f"Error: {e}")
    return await message.reply(f"{len(ids)} admin {'id' if len(ids)==1 else 'ids'} have been promoted!!\n\nSend /add_admin to add any id and /admins to check admin list.")

@Client.on_message(filters.command("admins") & filters.private)
async def add_new_admins(client, message):
    if not message.from_user.id in client.admins:
        return await message.reply(client.reply_text)
    return await message.reply(f"**Admin List:** `{client.admins}`")



