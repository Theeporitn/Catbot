# Dialogues by @Surv_ivor and @Sathan_Of_Telegram
import asyncio
import random

from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern=r"dgs$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"dgs$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "ഡയലോഗ് പറയുന്നു....")
    await asyncio.sleep(1)
    x = random.randrange(1, 91)
    if x == 1:
        await event.edit(
            "🎶 ഈ പൂട്ടിനു മേൽ നീ പൂട്ട് പൂട്ടിയാൽ നിന്നെ ഞാൻ പൂട്ടും ഒടുക്കത്തെ പൂട്ട് ഊതരുതെ ഊതിയാൽ തീപൊരി പറക്കും 🎶"
        )
    if x == 2:
        await event.edit(
            "🎶 എന്റെ ഭീഷണി എന്ന് പറഞ്ഞാൽ ചില ഊച്ചാളി പോലിസ്കാരെ പോലെ സ്ഥലം മാറ്റി കളയും എന്നല്ല കൊന്നു കളയും പുതിയ ആൾ ആയതു കൊണ്ടാ ഇവിടെ ചോതിച്ചാൽ മതി... 🎶"
        )
    if x == 3:
        await event.edit("🎶 സാധനം കയിൽ ഉണ്ടോ ?. 🎶")
    if x == 4:
        await event.edit("🎶 മോനെ അപ്പ ചട്ടിയിൽ വറക്കലെ🎶")
    if x == 5:
        await event.edit(
            "🎶 )മഴ കാലത്ത് മണ്ണിര ഒന്ന് കൊഴുത്ത് എന്ന് വിചാരിച്ചു മൂർക്കൻ പാമ്പിന്റെ വീട്ടിൽ പെണ്ണ് ആലോചിക്കാൻ വരല്ലേ... 🎶"
        )
    if x == 6:
        await event.edit("🎶 കൊച്ചിന്റെ തന്ത ആരാ എന്ന് ചോതിക്കു ഡാ ഡി.. 🎶")
    if x == 7:
        await event.edit(
            "🎶 വാ വിട്ട വാക്കും കയ് വിട്ട ആയുധം വിനാശത്തിനു ഓർത്താൽ നന്ന്... 🎶"
        )
    if x == 8:
        await event.edit("🎶 നമ്മുക്ക് ഒരു ഒന്ന് ഒന്നൊര ചോദ്യം ഉണ്ട് എന്ന് പറ... 🎶")
    if x == 9:
        await event.edit("🎶 ആദ്യം അടി പിന്നെ ഡയലോഗ്... 🎶")
    if x == 10:
        await event.edit("🎶 ആകാശത്തിനു ചുവട്ടിലെ ഏതു മണ്ണും ജഗ നാതനു സമം ആണ് 🎶")
    if x == 11:
        await event.edit("🎶 ടൈം ഇല്ലായിരുന്നു സർ ഒരു പാട് പെണ്ണ് അങ്ങനെ മിസ്സ്ചെയ്തു 🎶")
    if x == 12:
        await event.edit(
            "🎶 ചതിക്കും വഞ്ചനക്കും ഒറ്റ ശിക്ഷയെ ഉള്ളു അത് ഞാൻ ആയാലും ശരി നീയാലും🎶"
        )
    if x == 13:
        await event.edit("🎶 ദേവൻ ദേവ രാജൻ ദേവ രാജാ പ്രതാപ വർമ. 🎶")
    if x == 14:
        await event.edit("🎶 എത്ര മനോഹരമായ ആചാരങ്ങൾ... 🎶")
    if x == 15:
        await event.edit(
            "🎶 ഒരാളെ പോലെ ഏഴു പേർ ഉണ്ടെന്നു പറയുന്നത്തെറ്റാ ഒരാളെ പോലെ ഒരാളെ ഉള്ളു 🎶"
        )
    if x == 16:
        await event.edit("🎶 അപ്പോൾ നീ ആണ ല്ലേ പേൾ ഹാർബർ 🎶")
    if x == 17:
        await event.edit("🎶 എന്താടോ വാര്യരെ നന്നാവത്തെ. 🎶")
    if x == 18:
        await event.edit(
            "🎶 )സാഗർ എന്ന് മിത്രതെയെ നിനക്കറിയു ജാക്കി എന്ന ശത്രുവിനെ നിനക്ക് അറിയില്ല.. 🎶"
        )
    if x == 19:
        await event.edit("🎶മൈ നമ്പർ ഈസ് 2255 🎶")
    if x == 20:
        await event.edit(
            "🎶 എന്റെ തലയ്ക്കു മീതെ ഒരു പരന്തും പറകില്ല പറന്നാൽ തല അരിയും 🎶"
        )
    if x == 21:
        await event.edit("🎶 യമനോട് ആരും ആയുസ്സ് ചോതികാറില്ല... 🎶")
    if x == 22:
        await event.edit("🎶 എന്റെ റോള് അത് മറ്റ്റാർക്കും കഴിയില്ല 🎶")
    if x == 23:
        await event.edit(
            "🎶 അമ്പലപ്പുഴെ ഉണ്ണിക്കണ്ണനോടു നീ... എന്തുപരിഭവം മെല്ലെയോതിവന്നുവോ... 🎶"
        )
    if x == 24:
        await event.edit(
            "🎶 അഹങ്കാരത്തിനു കയും കാലും വയ്ക്ക എന്നിട്ട് പെണ് എന്ന് പേരും 🎶"
        )
    if x == 25:
        await event.edit("🎶 എങ്കിൽ തോമ മുടി നീട്ടി വളർത്തും ചുര്ക്കാൻ.. 🎶")
    if x == 26:
        await event.edit("🎶 നീ തങ്ങത്തില്ല. 🎶")
    if x == 27:
        await event.edit("🎶 എന്നാ എന്നോട് പറ ഐ ലവ് യു എന്ന്. 🎶")
    if x == 28:
        await event.edit("🎶 കിണ്ടി .. കിണ്ടി.. 🎶")
    if x == 29:
        await event.edit(
            "🎶 ഈ നെട്ടുരാൻ വിളിച്ചതിൽ കൂടുതൽ മുദ്രവാക്യം ഒന്നും സേതു വിളിച്ചിട്ടില്ല... 🎶"
        )
    if x == 30:
        await event.edit("🎶 കയ് എട് ഭാസ്കരാ... 🎶")
    if x == 31:
        await event.edit("🎶 ജീവിക്കാൻ ഉള്ള ആഗ്രഹം കൊണ്ട്ചോതിക്കാ ഇല്ലാലെ... 🎶")
    if x == 32:
        await event.edit("🎶 തോമ ചെറ്റയല്ല... 🎶")
    if x == 33:
        await event.edit("🎶 തോമ വിചാരിച്ചു തോമ മാത്രമ ആണ്കുട്ടി എന്ന് തെറ്റി... 🎶")
    if x == 34:
        await event.edit(
            "🎶 ആ രഹസ്യം ഞാൻ മരിക്ക്കുമ്പോൾ എന്നോട് കൂടെ മന്നി ചേരും അതാണ് ഞാൻ നിങ്ങള്ക്ക് നല്കുന്നഏറ്റവും വലിയ സുരക്ഷ...🎶"
        )
    if x == 35:
        await event.edit("🎶 ഇത് എന്താടാ പഴുപിക്കാൻ ആഹ് ?... 🎶")
    if x == 36:
        await event.edit("🎶 ഇതാണോ നീ പറഞ്ഞ patient..🎶")
    if x == 37:
        await event.edit("🎶 മിഥുനം കര്കിടകം മിഥുനത്തിൽ ഒഴിവു പിന്നെ അശോകനും......🎶")
    if x == 38:
        await event.edit("🎶 വട്ടാണല്ലേ..🎶")
    if x == 39:
        await event.edit(
            "🎶 ഈ നഗരം ഉള്ളിടത്തോളം നിന്നോട് പറയാൻ ബാക്കി വെച്ച ആ വാക്കുകളുമായി ഞാൻ കാത്തുനിൽക്കും.... 🎶"
        )
    if x == 40:
        await event.edit("🎶 മേ ഹൂം ഉസ്താദ്...🎶")
    if x == 41:
        await event.edit("🎶 എല്ലാം അറിയുന്നവാൻ ഞാൻ ശംഭോ മഹാ ദേവാ...🎶")
    if x == 42:
        await event.edit("🎶 ഞെട്ടാൻ റെഡി ആയി ഇരുന്നോട്ട .... 🎶")
    if x == 43:
        await event.edit(
            "🎶 തോല്ക്കുനതിനു തൊട്ട് മുൻപ് വരെ ശുഭാപ്തി വിശ്വാസം നല്ലതാണ്...🎶"
        )
    if x == 44:
        await event.edit("🎶 നാളെ മുതൽ ആകാശത്തിലെ പുതിയ നക്ഷത്രം ഞാൻ ആയിരിക്കും...🎶")
    if x == 45:
        await event.edit("🎶 ഗോവിന്ദൻ കുട്ടി ആ കുട്ടി മിണ്ടുന്നില്ല🎶")
    if x == 46:
        await event.edit(
            "🎶 കാണം സാറേ നല്ലേ മീൻ നാറ്റം ഉണ്ട് കുളിച് മിടുക്കൻ ആയി ഇരിക്ക് പണി ഞാൻ തരുന്ന്ട്... 🎶"
        )
    if x == 47:
        await event.edit(
            "🎶 ചീപ് ഷ്യ്നിങ്ങ് ആണ് എന്ന് വിചാരികരുത് വാട്ച് ഇത്തിരി കോസ്റ്റ് ലി ആണ് 🎶"
        )
    if x == 48:
        await event.edit("🎶 കർത്താവേ കിട്ടി കാണുമോ... 🎶")
    if x == 49:
        await event.edit("🎶 ഒടകാൻ നില്കണ്ട കണ്ടാലറിയാം ചെറ്റയാ....  🎶")
    if x == 50:
        await event.edit("🎶 ഷോ ഷോ...🎶")
    if x == 51:
        await event.edit("🎶 നീ പോ മോനെ ദിനേശാ...🎶")
    if x == 52:
        await event.edit("🎶 പോയ കാലം ആണ് രഗുവേട്ടാ ഒഴിഞ്ഞ കല്പക തുണ്ടുകൾ...🎶")
    if x == 53:
        await event.edit("🎶 മുട്ടനാടിന്റെ ചങ്കിലെ ചോര അതാണ് എന്റെ ജീവൻ ടോണ്...  🎶")
    if x == 54:
        await event.edit(
            "🎶 8 വയ്യസിൽ കോപം വന്നാൽ നീ കല്ലെടുക്കും നാൻ കത്തി താൻ എടുക്കെ... 🎶"
        )
    if x == 55:
        await event.edit("🎶 ശിവ ഇല്ലാമേ ശക്തി ഇല്ല...🎶")
    if x == 56:
        await event.edit("🎶 കിട്ടിയാൽ നീ എന്നെ ഒലത്തും...🎶")
    if x == 57:
        await event.edit(
            "🎶 നീീ പോയി കാഴ്ച്ചകാരെ കൂട്ടു ഞാൻ എത്തും എന്റെ പേര് ജഗനാതൻ എന്നാ 🎶"
        )
    if x == 58:
        await event.edit(
            "🎶 ഈ വേലായുധനെ തല്ലി തോപ്പിക്കാൻ ചക ഉറപ്പ് ഉള്ള ഉണ്ടെങ്കിൽ വാടാ... 🎶"
        )
    if x == 59:
        await event.edit("🎶 കര്ത്താവേ കിട്ടി കാണുമോ... 🎶")
    if x == 60:
        await event.edit(
            "🎶 ഈ ഇരുട്ട് നിറഞ്ഞ എന്റെ ജീവിത്തിലേക്ക് തകര്ച്ചയെ ഓര്മിപിക്കാൻ നീ എന്തിനു വന്നു 🎶"
        )
    if x == 61:
        await event.edit(
            "🎶 വില കൊടുത്താലും കിട്ടാൻ പാട് ഉള്ള ലിവർ അല്ല ജോണ് സാ നാം തകരുകുന്നത്... 🎶"
        )
    if x == 62:
        await event.edit(
            "🎶 അവൻ മാര് ഒന്ന് വിരല അമർത്തിയാൽ നിന്റെ അപ്പൻ അപ്പൂപ്പൻ മാരുടെ ഫോസിൽ വരെ തകര്ന്നു പോകും...🎶"
        )
    if x == 63:
        await event.edit("🎶 ഈ ഒരു പ്രാവശ്യം എങ്കിലും എനിക്ക് ജയിക്കണം... 🎶")
    if x == 64:
        await event.edit(
            "🎶 നീ പിള്ളേരും കൂട്ടി സ്ഥലം വിട് വയ്കും മുന്പ് വീട്ടില് എത്താം... 🎶"
        )
    if x == 65:
        await event.edit("🎶 എന്നോട് കളിക്കല്ലേ ഞാൻ കളി പടിപിക്കും... 🎶")
    if x == 66:
        await event.edit(
            "🎶 ഒരിക്കൽ നീയെന്നെ വേദനിപിച്ചാ പോയത് സമയം എടുത്ത് \ അത് മറക്കാൻ...🎶"
        )
    if x == 67:
        await event.edit(
            "🎶 അവൾക്കു ഇഷ്ടല്ല വേണ്ട എനിക്ക് ഇഷ്ട്ടാ അവളെ മാത്രം അല്ല കാണാൻ കൊള്ളാവുന്ന എല്ലാവരെയും...🎶"
        )
    if x == 68:
        await event.edit(
            "🎶 അവൾക്കു ഇഷ്ടല്ല വേണ്ട എനിക്ക് ഇഷ്ട്ടാ അവളെ മാത്രം അല്ല കാണാൻ കൊള്ളാവുന്ന എല്ലാവരെയും ... 🎶"
        )
    if x == 69:
        await event.edit("🎶 പോരുന്നു എന്റെ കൂടെ...🎶")
    if x == 70:
        await event.edit(
            "🎶 മനസിൽ കുറ്റ ബോധം വന്നാൽ ചെയ്യുന്നത് എല്ലാം യാന്തിർകം ആകും...🎶"
        )
    if x == 71:
        await event.edit("🎶 പൂകോയി മോനെ നീ കൊച്ചിനു ആളിരിക്കി എന്നെ തല്ലുമോട...🎶")
    if x == 72:
        await event.edit("🎶 ആരും തല്ലരുത് ഇവനെ ഇവനെ എനിക്ക് ഒറ്റയ്ക്ക് തല്ലണം... 🎶")
    if x == 73:
        await event.edit("🎶 ആരും തല്ലരുത് ഇവനെ ഇവനെ എനിക്ക് ഒറ്റയ്ക്ക് തല്ലണം... 🎶")
    if x == 74:
        await event.edit("🎶 സ്കൂൾ ആണ് മറ്റു അധ്യാപകർ ഉണ്ട് കരയരുത്... 🎶")
    if x == 75:
        await event.edit("🎶 മോള് ഈ ബോംബെ എന്ന് കേട്ടിടുണ്ടോ... 🎶")
    if x == 76:
        await event.edit("🎶 ലേലു അല്ല് ലേലു എന്നെ വെറുതെ വിട്...🎶")
    if x == 77:
        await event.edit("🎶 ഒരു മുത്ത് കൌ..🎶 ")
    if x == 78:
        await event.edit("🎶 ക്യാമറ മാൻ വേനുവിനെടോപ്പം ഇനിയെന്നും രേണുക...🎶")
    if x == 79:
        await event.edit("🎶 ഇന്നലെയും മഴ ഉണ്ടായിരുന്നു അവയൊന്നും എന്റെ തായിരുനില്ല...🎶")
    if x == 80:
        await event.edit(
            "🎶 വൃദ്ധനെ പോലും പതിനാറു കാരൻ ആക്കുന്ന അസുരാൻപോലും സ്വപനം കാണാൻ പടിപിക്കുന്ന പ്രണയം...🎶"
        )
    if x == 81:
        await event.edit("🎶 തെങ കുടിക്കുന്നു പറക്കുന്നു പരാഗണം...")
    if x == 82:
        await event.edit("🎶 ഒരു കിംഗ് ഫിഷേർ ചില്ലെട്...🎶")
    if x == 83:
        await event.edit(
            "🎶 ഈ വാച്ചിന്റെ നമ്പറ ഞാൻ കുറെ തവണ ചെയ്തിട്ടുണ്ട് അത് കൊണ്ട് ഇത് ഇവടെ കിടക്കട്ടെ...🎶"
        )
    if x == 84:
        await event.edit("🎶 സബാണോ കി സിദ്നഗി ........🎶")
    if x == 85:
        await event.edit("🎶 ഉണ്ടായിരുന്ന എനർജി എല്ലാം ഇന്നലെ തീര്ന്നു...")
    if x == 86:
        await event.edit("🎶 സോറി ഇൻസ്പെക്ടർ നിങ്ങള്ക്ക് എന്നെ തോല്പിക്കാൻ ആവില്ല...")
    if x == 87:
        await event.edit("🎶 മണിയ നീ പോ...")
    if x == 88:
        await event.edit("🎶 ശ്രീ ഹളിയിലെക്കുള്ള വളി...")
    if x == 89:
        await event.edit(
            "🎶 ഹരിക്കുബോലും ഗുനികുമ്പോഴും ഒത്തരം ശരി ആയാലും ഒന്നൂടെ നോക്കുനത് അല്ലേ നല്ലത്..."
        )
    if x == 90:
        await event.edit("🎶 അപ്പ് ഇവിടെ ഒക്കെ കാണില്ലേ...🎶")
    if x == 91:
        await event.edit(
            "🎶 വെള്ളമടിച്ചു കോണ് തിരിഞ്ഞു വീട്ടില് വരുമ്പോൾ ചുമ്മാ കാൽ മടക്കി തോഴിക്കാനും തുലാ വര്ഷ രാത്രിയിൽ ഒരു പുതപ്പിനടിയിൽ സ്നേഹിക്കാനും എനിക്ക് ഒരു പെണ്ണിനെ വേണം വില്ൽ യു മൈ ഗേൾ !!!"
        )
