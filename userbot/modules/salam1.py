# Gausah kesini ngentot!!
# NGEDIT CMD YG BENER KONTOL!!!


from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^.gjn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Gajelas Lu BEGO")


@register(outgoing=True, pattern='^.yb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Yabenarrrrrrr ahh...**")


@register(outgoing=True, pattern='^.m(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**M*MEK NYA ANAK INIIIII....**")


@register(outgoing=True, pattern='^.k(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Apalo BEGO....**")


@register(outgoing=True, pattern='^.gjb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAJELAS BABI....**")


@register(outgoing=True, pattern='^.gjk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Gajelas Lu K*NTOL....**")


@register(outgoing=True, pattern='^.gbgn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ga banget, BEGO!!!**")


@register(outgoing=True, pattern='^.gls(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK, LO SANGEAN!!!**")


@register(outgoing=True, pattern='^.bsl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GA BAU TANAH LO..!!**")


@register(outgoing=True, pattern='^.hai(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Hai, SALKEN SAYA AR!!**")


@register(outgoing=True, pattern='^.nj(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Najis Anj*ng Muka lo Kek Kont*l...!!!**")


@register(outgoing=True, pattern='^.ds(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DESAH AH AH AH AWOKWOKWOK, CANDA**")


@register(outgoing=True, pattern='^.ucp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Lu siapa si BEGO SO KENAL!!!!**")


@register(outgoing=True, pattern='^.hey(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Hey, Member Alay..😂**")


@register(outgoing=True, pattern='^.loh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LOH LAH LOH, KE ORANG BEGO AJA LU GUA LAT!!🤣**")
    


CMD_HELP.update({
    "salam3":
    ".gjm\
\nUsage:\
\n\n.gjn\
\nUsage:\
\n\n.gjb\
\nUsage:\
\n\n.yb\
\nUsage:\
\n\n.gjk\
\nUsage:"
})

CMD_HELP.update({
    "salam4":
    ".gbgn\
\nUsage:\
\n\n.bsl\
\nUsage:\
\n\n.hai\
\nUsage:\
\n\n.ds\
\nUsage:\
\n\n.nj\
\nUsage:\
\n\n.gls\
\nUsage:\
\n\n.hey\
\nUsage:\
\n\n.loh\
\nUsage:\
\n\n.ucp\
\nUsage:\
\n\n.m\
\nUsage:\
\n\n.k\
\nUsage:\
\n\n.psos\
\nUsage:"
})
