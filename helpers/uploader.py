import asyncio
import os
import time

from __init__ import LOGGER
from bot import LOGCHANNEL, userBot
from config import Config
from pyrogram import Client
from pyrogram.types import CallbackQuery, Message

from helpers.display_progress import Progress


async def uploadVideo(
    c: Client,
    cb: CallbackQuery,
    merged_video_path,
    width,
    height,
    duration,
    video_thumbnail,
    file_size,
    upload_mode: bool,
):
       
    # Report your errors in telegram (@StupidBoi69).
    if Config.IS_PREMIUM:
        sent_ = None
        prog = Progress(cb.from_user.id, c, cb.message)
        async with userBot:
            if upload_mode is False:
                c_time = time.time()
                sent_: Message = await userBot.send_video(
                    chat_id=int(LOGCHANNEL),
                    video=merged_video_path,
                    height=height,
                    width=width,
                    duration=duration,
                    thumb=video_thumbnail,
                    caption=f"""<b>
{merged_video_path.rsplit('/',1)[-1]}


<u>User's Information:</u>
-Bot: @{Config.BOT_USERNAME}
-User Link: <a href='tg://user?id={cb.from_user.id}'><b>Click Here</b></a>
-Username: @{cb.from_user.username}
-User's ID: {cb.from_user.id}</b>""",
                    progress=prog.progress_for_pyrogram,
                    progress_args=(
                        f"<b>Uploading:\n{merged_video_path.rsplit('/',1)[-1]}</b>",
                        c_time,
                    ),
                )
            else:
                c_time = time.time()
                sent_: Message = await userBot.send_document(
                    chat_id=int(LOGCHANNEL),
                    document=merged_video_path,
                    thumb=video_thumbnail,
                    #caption=f"<b>{merged_video_path.rsplit('/',1)[-1]}\n\n\n<u>User's Information:</u>\n-{cb.from_user.mention}\n-{cb.from_user.id}</b>",
                    caption=f"""<b>
{merged_video_path.rsplit('/',1)[-1]}


<u>User's Information:</u>
-Bot: @{Config.BOT_USERNAME}
-User Link: <a href='tg://user?id={cb.from_user.id}'><b>Click Here</b></a>
-Username: @{cb.from_user.username}
-User's ID: {cb.from_user.id}</b>""",
                    progress=prog.progress_for_pyrogram,
                    progress_args=(
                        f"<b>Uploading:\n{merged_video_path.rsplit('/',1)[-1]}</b>",
                        c_time,
                    ),
                )
            if sent_ is not None:
                await c.copy_message(
                    chat_id=cb.message.chat.id,
                    from_chat_id=sent_.chat.id,
                    message_id=sent_.id,
                    caption=f"<b>{merged_video_path.rsplit('/',1)[-1]}</b>",
                )
                # await sent_.delete()
    else:
        try:
            sent_ = None
            prog = Progress(cb.from_user.id, c, cb.message)
            if upload_mode is False:
                c_time = time.time()
                sent_: Message = await c.send_video(
                    chat_id=cb.message.chat.id,
                    video=merged_video_path,
                    height=height,
                    width=width,
                    duration=duration,
                    thumb=video_thumbnail,
                    caption=f"""<b>
{merged_video_path.rsplit('/',1)[-1]}


<u>User's Information:</u>
-Bot: @{Config.BOT_USERNAME}
-User Link: <a href='tg://user?id={cb.from_user.id}'><b>Click Here</b></a>
-Username: @{cb.from_user.username}
-User's ID: {cb.from_user.id}</b>""",
                    progress=prog.progress_for_pyrogram,
                    progress_args=(
                        f"<b>Uploading:\n{merged_video_path.rsplit('/',1)[-1]}</b>",
                        c_time,
                    ),
                )
            else:
                c_time = time.time()
                sent_: Message = await c.send_document(
                    chat_id=cb.message.chat.id,
                    document=merged_video_path,
                    thumb=video_thumbnail,
                    caption=f"**{merged_video_path.rsplit('/',1)[-1]}**",
                    progress=prog.progress_for_pyrogram,
                    progress_args=(
                        f"<b>Uploading:\n{merged_video_path.rsplit('/',1)[-1]}</b>",
                        c_time,
                    ),
                )
        except Exception as err:
            LOGGER.info(err)
            await cb.message.edit("Failed to upload")
        if sent_ is not None:
            if Config.LOGCHANNEL is not None:
                media = sent_.video or sent_.document
                await sent_.copy(
                    chat_id=int(LOGCHANNEL),
                    caption=f"""<b>
{media.file_name}


<u>User's Information:</u>
-Bot: @{Config.BOT_USERNAME}
-User Link: <a href='tg://user?id={cb.from_user.id}'><b>Click Here</b></a>
-Username: @{cb.from_user.username}
-User's ID: {cb.from_user.id}</b>"""
                    #caption=f"<b>\n\n\n<u>User's Information:</u>\n-{cb.from_user.mention}\n-{cb.from_user.id}</b>",                    
                )


async def uploadFiles(
    c: Client,
    cb: CallbackQuery,
    up_path,
    n,
    all
):
    try:
        sent_ = None
        prog = Progress(cb.from_user.id, c, cb.message)
        c_time = time.time()
        sent_: Message = await c.send_document(
            chat_id=cb.message.chat.id,
            document=up_path,
            caption=f"**{up_path.rsplit('/',1)[-1]}**",
            progress=prog.progress_for_pyrogram,
            progress_args=(
                f"<b>Uploading: {up_path.rsplit('/',1)[-1]}</b>",
                c_time,
                f"\n<b>Uploading: {n}/{all}</b>"
            ),
        )
        if sent_ is not None:
            if Config.LOGCHANNEL is not None:
                media = sent_.video or sent_.document
                await sent_.copy(
                    chat_id=int(LOGCHANNEL),
                    caption=f"""<b>
{media.file_name}


<u>User's Information:</u>
-Bot: @{Config.BOT_USERNAME}
-User Link: <a href='tg://user?id={cb.from_user.id}'><b>Click Here</b></a>
-Username: @{cb.from_user.username}
-User's ID: {cb.from_user.id}</b>""",
                    #caption=f"<b>{media.file_name}\n\n\n<u>User's Information:</u>\n-{cb.from_user.mention}\n-{cb.from_user.id}</b>",
                )
    except:
        1    
    1
