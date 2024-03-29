import discord, re, os
from discord.ext import commands

class Jojo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.references = re.compile(r"breath|stand|oh my god|dio|holy shit|son of a bitch|\bstar\b|platinum|world|chariot|magician|\bred\b|silver|purple|hermit|heirophant|\bgreen\b|fool|\bsun\b|\bkars\b|diamond|crazy|killer|queen|chili|pepper|stray cat|kira|yoshikage|hayato|pearl jam|harvest|enigma|heaven's door|hand\b|gold|experience|sticky fingers|zipper|echo|king crimson|requiem|crusade|mask|pillar|awaken|tommy gun|vampire|arrow|superfly|jojo|bizarre|adventure|menacing|turtle|zeppeli|joseph|jonathan|jotaro|josuke|golden ratio|for one reason|stair|ora|muda|useless|egypt|aerosmith|moody blues|lovers|emperor|temperance|death|thirteen|justice|strength|boat|ambulance|train|\block|cinderella|crash|baby face|metallica|green day|rolling stone|notorious|big|chase|great days|end of the world|oasis|sex pistols|brando|kujo|joestar|hot foot|hotfoot|part [1-8]|hol horse|cream|giorno|jolyne|johnny|diavolo|pucci|valentine|rokakaka|rohan|okuyasu|lisa|koichi|polnareff|kakyoin|caesar|speedwagon|morioh|bruno|bucciarati|mista|narancia|abbacchio|trish|passione|valkyrie|slow dancer|silver bullet|gets up|ghost rider|hey ya|hono|foxy lady|little wing|crosstown traffic|el condor pasa|europe express|\bpeg\b|ramblin' man|roxanne|moon flower|nut rocker|country grammar|catch a wave|love unlimited|natalie|black rose|steel ball run|stardust|giovanna|phantom blood|battle tendency|diamond is unbreakable|no weaknesses|vento aureo|stone ocean|araki|danny|poco|tonpetty|dire|straizo|erina|george|tattoo|bruford|wang chan|jack the ripper|tarkus|adams|doobie|dario|elizabeth|mary|stroheim|messina|loggins|smokey|suzi q|acdc|esidisi|wammu|santana|donovan|mark|mario|muhammad|abdol|iggy|holly|\banne\b|roses|enya|vanilla ice|nukesaku|d'arby|pet shop|n'doul|mariah|alessi|oingo|boingo|anubis|kenny g|steely dan|sherry|reimi|shigeki|mikitaka|hazekura|yukako|yamagishi|yuya|fungami|tamami|kobayashi|toshikazu|hazamada|tonio|trussardi|aya|tsuji|shizuka|tama|keicho|akira|otoishi|anjuro|katagiri|coco jumbo|doppio|pericolo|ohmygod|jesus|warudo|emerald spash|it just works|you're approaching me|wry|roundabout|Catch the rainbow|thunder cross split attack|coffee flavored gum|oh thats a baseball|jaggers|red dragons|f mega|nigerundayo|styx|Dan of steel|kiss|foo fighters|Marilyn manson|highway to hell|weather report|c moon|whitesnake|diver down|Dragon's dream|burning down the house|Goo goo dolls|Jumpin' jack flash|Limp bizkit|Manhattan transfer|Survivor|Yo-yo ma|Mozzarella|\b13\b|Arts and crafts|disney|baseball|Disney|Organism that has sex|Marilyn Manson|Limp Bizcuit|Eat Shit|Pizza Mozarella|Bug Bites|Jesus Christ|Golden Ratio|Spin|Heavy Weather|Weather Report|My name is|Balls Deep|steel ball|Phantom|Aztec|This means war|Cracker Volley|Your underpants is showing|Yatazo|Bloody St|Fried Chicken|Johnny Depp|Vampire|Breathing|Stone Mask|Danny|Bread|North Wind|Vikings|Father Styx|Water|Capo|Torture dance|Smoke|rat", re.IGNORECASE)

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Startup] Cog Jojo loaded successfully')

    @commands.Cog.listener()
    async def on_message(self, message):
        check = self.references.search(message.content)
        if check != None:
            print("[Jojo] Is that a motherfucking Jojo's reference?! Matched text:", check)
            emoji = self.bot.get_emoji(439149499349205014)
            await message.add_reaction(emoji)

def setup(bot: commands.Bot):
    bot.add_cog(Jojo(bot))