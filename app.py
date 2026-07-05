print("Hello world")
import discord
from discord.ext import commands
from discord.activity import Game
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
)

intents = discord.Intents.default()
intents.messages = True
intents.members = True  # Enable intents to track members' voice states
intents.presences = True  # Ensure presences intent is enabled
# intents.guilds = True  # Enable intents to interact with guild information

bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)

#  print hello world


@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name}')


@client.event
async def on_ready():
    logging.info(f'Logged in as {client.user}')


@client.event
async def on_member_update(before, after):
    logging.info(f"before {before}")
    logging.info(f"after {after}")

@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(f'Hello {msg.author}!')

@client.event
async def on_message_edit(before, after):
    pass

# 디스코드 실행
# 디스코드 for Mac 종료:
## before.status Status.online              after.status: Status.offline
## before.desktop_status Status.online      after.desktop_status: Status.offline
## before.mobile_status Status.offline      after.mobile_status: Status.offline
@bot.event
async def on_presence_update(before, after):
    logging.info(f"before {before} {before.status} {before.desktop_status} {before.mobile_status} {before.is_on_mobile()}")
    logging.info(f"after {after} {after.status} {after.desktop_status} {after.mobile_status} {after.is_on_mobile()}")

# 화면 공유 시작
# 화면 공유 종료
# 카메라 공유 시작
# 카메라 공유 종료
@bot.event
async def on_voice_state_update(member, before, after):
    # Check if a member starts sharing their camera
    if not before.self_video and after.self_video:
        logging.info(f'{member} started sharing their camera in {after.channel.name}.')
    1113887875310813307
    # Check if a member stops sharing their camera
    elif before.self_video and not after.self_video:
        logging.info(f'{member} stopped sharing their camera in {before.channel.name}.')

    # Check if a member starts streaming
    if not before.self_stream and after.self_stream:
        logging.info(f'{member} started streaming in {after.channel.name}.')

    # Check if a member stops streaming
    elif before.self_stream and not after.self_stream:
        logging.info(f'{member} stopped streaming in {before.channel.name}.')


@bot.command()
async def check_game(ctx, member: discord.Member):
    discord.game
    # Check if the member is playing a game
    if member.activity and isinstance(member.activity, discord.Game):
        game = member.activity
        message = f"{member.name} is currently playing {game.name}."

        # Check if the platform information is available (new in version 2.4)
        if hasattr(game, 'platform') and game.platform:
            message += f" Platform: {game.platform}."

        # Check if the game start time is available
        if hasattr(game, 'start') and game.start:
            message += f" Started playing at: {game.start.strftime('%Y-%m-%d %H:%M:%S UTC')}."

        # Optionally, you can also include information about game assets like images
        if hasattr(game, 'assets') and game.assets:
            large_image = game.assets.get('large_image', 'No large image')
            message += f" Large Image ID: {large_image}."

        await ctx.send(message)
    else:
        await ctx.send(f"{member.name} is not playing a game right now.")


# Replace 'your_bot_token_here' with your actual bot token
bot.run('YOUR_BOT_TOKEN_HERE')

[자료] 2023_BIOLOGY BASIC 1st 추가자료
0분
0%
수강 전
자료
[자료] 2023_BIOLOGY BASIC 2nd 추가자료
0분
0%
수강 전
자료
01
[1회차]Ch.01 생명현상의 특성_2.과학적 탐구 방법론 p2~4
81분
40%
25.06.08 20:48:28
02
[1회차]Chapter.02 생명체의 화학적 구성_1.원자(1) ~p14
57분
100%
25.06.08 21:27:18
03
[1회차]Chapter.02 생명체의 화학적 구성_1.원자(2) ~p14
28분
90%
25.06.08 22:00:51
04
[1회차]Chapter.03 생명체의 구성분자들_2.co탄수화물 특징 ~p25
104분
90%
25.06.09 23:07:09
05
[2회차]2.유기분자들 (1)탄수화물 ②종류 ii)다당류 p.31
102분
90%
25.06.11 21:29:12
06
[2회차]2.유기분자들 (3)단백질 ③단백질 iv)4차구조 p.37 (1)
42분
90%
25.06.11 22:08:57
07
[2회차]2.유기분자들 (3)단백질 ③단백질 iv)4차구조 p.37 (2)
37분
0%
수강 전
08
[2회차]2.효소의 기능과 구조 (2)효소의구조 *동종효소 p.58
97분
0%
수강 전
09
[3회차](3)반응속도론 ~p.63
93분
0%
수강 전
10
[3회차]크로마토그래피-이온교환크로마토그래피 ~p.71(1)
47분
0%
수강 전
11
[3회차]크로마토그래피-이온교환크로마토그래피 ~p.71(2)
33분
0%
수강 전
12
[3회차]지질을 통한 수송-삼투현상 ~p.93
103분
0%
수강 전
13
[4회차](2)막단백질을 통한수송-소장상피세포의 포도당흡수 기작 p.95
101분
0%
수강 전
14
[4회차]06.세포내 소기관 내부공생설 p.110(1)
38분
0%
수강 전
15
[4회차]06.세포내 소기관 내부공생설 p.110(2)
46분
0%
수강 전
16
[4회차]06.(3)세포의 구조와 소기관-협막과 점액층 p.119
101분
0%
수강 전
17
[5회차]06장. ~③골지체 p.124
99분
0%
수강 전
18
[5회차]06장. ~세포분열과 방추사 p.130 (1)
36분
0%
수강 전
19
[5회차]06장. ~세포분열과 방추사 p.130 (2)
40분
0%
수강 전
20
[5회차]06장. ~원핵생물과 진핵생물의 비교 p.143
99분
0%
수강 전
21
[6회차]07. ~ 해당과정 p.162
98분
0%
수강 전
22
[6회차]07. F0F1 복합체저해제 p.170 (1)
39분
0%
수강 전
23
[6회차]07. F0F1 복합체저해제 p.170 (2)
50분
0%
수강 전
24
[6회차]07. 아미노산의 산화 p.178
92분
0%
수강 전
25
[7회차]조류의 흡광파장 p.197
101분
0%
수강 전
26
[7회차](2)광합성에 미치는 요인 ① 빛의 세기 p.202 (1)
39분
0%
수강 전
27
[7회차](2)광합성에 미치는 요인 ① 빛의 세기 p.202 (2)
48분
0%
수강 전
28
[7회차]세포분열-(4)인간의 염색체 p.223
94분
0%
수강 전
29
[8회차]9장 - 세포질분열(식물세포) p.230
98분
0%
수강 전
30
[8회차]9장 - 세포분열 p.235 (1)
34분
0%
수강 전
31
[8회차]9장 - 세포분열 p.235 (2)
45분
0%
수강 전
32
[8회차]10장 유전학 (2)멘델유전법칙 예외 0 공동우성 p.253
79분
0%
수강 전
33
[9회차]10-③ 반성유전 p.258
99분
0%
수강 전
34
[9회차]10-이형접합자와 열성 순종교배 p.264(1)
38분
0%
수강 전
35
[9회차]10-이형접합자와 열성 순종교배 p.264(2)
48분
0%
수강 전
36
[9회차]11-11)유전물질의 추적 p.290
87분
0%
수강 전
37
[10회차]11강 (2)DNA 복제과정 ②진행 p.296
102분
0%
수강 전
38
[10회차]11강 끝까지 - DNA 지문법까지 p.303 (1)
50분
0%
수강 전
39
[10회차]11강 끝까지 - DNA 지문법까지 p.303 (2)
31분
0%
수강 전
40
[10회차]12강 (2)전사의 과정 (ii)진핵생물까지 p.326
90분
0%
수강 전
41
[11회차]3-번역, 워블가설 p.332
104분
0%
수강 전
42
[11회차]13장-①바이러스 p.354 (1)
29분
0%
수강 전
43
[11회차]13장-①바이러스 p.354 (2)
56분
0%
수강 전
44
[11회차]13장-HIV바이러스 p.361
78분
0%
수강 전
45
[12회차]회전환복제 p.367
98분
0%
수강 전
46
[12회차]세포 특이적 유전자의 전사 p.387 (1)
29분
0%
수강 전
47
[12회차]세포 특이적 유전자의 전사 p.387 (2)
63분
0%
수강 전
48
[12회차]염색체 구조이상 돌연변이 p.401
78분
0%
수강 전
49
[13회차]15 - 돌연변이 ④삽입물질 p.405
97분
0%
수강 전
50
[13회차]16 - 재조합 대장균 선별과정(2링16.09) p.422 (1)
35분
0%
수강 전
51
[13회차]16 - 재조합 대장균 선별과정(2링16.09) p.422 (2)
53분
0%
수강 전
52
[13회차]16 - (3) 게놈 프로젝트 p.430
69분
0%
수강 전
53
[14회차]체세포복제 그림16.30 p.436
98분
0%
25.06.08 14:17:54
54
[14회차]수용체 단백질 분류 2권 p.13 (1)
40분
0%
25.06.08 14:19:53
55
[14회차]수용체 단백질 분류 2권 p.13 (2)
45분
0%
25.06.08 14:19:07
56
[14회차]18. 세포신호전달계 p.21
76분
0%
수강 전
57
[15회차]19 발생학 (2) 난할 p.35
103분
0%
수강 전
58
[15회차]19 발생학 - 형성체의 축유도 p.41 (1)
24분
0%
수강 전
59
[15회차]19 발생학 - 형성체의 축유도 p.41 (2)
67분
0%
수강 전
60
[15회차]19 발생학 IPSC p.47
79분
0%
수강 전
61
[16회차]제19발생학 - 체절생성 및 분화 그림 19.36 p.52
94분
0%
수강 전
62
[16회차]남성생식계 p.77 (1)
39분
0%
수강 전
63
[16회차]남성생식계 p.77 (2)
53분
0%
수강 전
64
[16회차]20. 여성생식계 p.81
66분
0%
수강 전
65
[17회차]21 뉴런 - 기본개념들 p.98
99분
0%
수강 전
66
[17회차]21 뉴런 - (3)축삭돌기의 신호전달 p.102 (1)
50분
0%
수강 전
67
[17회차]21 뉴런 - (3)축삭돌기의 신호전달 p.102 (2)
37분
0%
수강 전
68
[17회차]22 신경계 - (2)교세포 분류 p.117
79분
0%
수강 전
69
[18회차]22 신경계 - ③기저핵까지 p.123
99분
0%
수강 전
70
[18회차]22-(2)운동신경 p.129 (1)
33분
0%
수강 전
71
[18회차]22-(2)운동신경 p.129 (2)
55분
0%
수강 전
72
[18회차]23 내분비계-(2) 호르몬의 종류 p.143
80분
0%
수강 전
73
[19회차]23 내분비계 호르몬 p.147
102분
0%
수강 전
74
[19회차]23 내분비계 (5)부갑상선 p.153 (1)
38분
0%
수강 전
75
[19회차]23 내분비계 (5)부갑상선 p.153 (2)
53분
0%
수강 전
76
[19회차]23단원 내분비계 호르몬 (7)부신 P.158
70분
0%
수강 전
77
[20회차]후각수용기 p.178
108분
0%
수강 전
78
[20회차]청각수용기 p.185 (1)
18분
0%
수강 전
79
[20회차]청각수용기 p.185 (2)
65분
0%
수강 전
80
[20회차]시각경로 p.193
73분
0%
수강 전
81
[21회차]③연축과 강축- 강축까지 p.216
104분
0%
수강 전
82
[21회차](2) 인체의 심장구조-26순환계 p.235 (1)
19분
0%
수강 전
83
[21회차](2) 인체의 심장구조-26순환계 p.235 (2)
69분
0%
수강 전
84
[21회차]심장주기 -26순환계 p.241
63분
0%
수강 전
85
[22회차]26. 순환계 - (6)정맥 p.246
95분
0%
수강 전
86
[22회차]26. 순환계 - (4)백혈구 p.252 (1)
48분
0%
수강 전
87
[22회차]26. 순환계 - (4)백혈구 p.252 (2)
41분
0%
수강 전
88
[22회차]27. 면역계 - (ii)대식세포 p.271
84분
0%
수강 전
89
[23회차]27. 면역계 - (3)항체 (v)IgE p.276
89분
0%
수강 전
90
[23회차]27. 면역계 - (5)TCR(T수용체) p.283 (1)
40분
0%
수강 전
91
[23회차]27. 면역계 - (5)TCR(T수용체) p.283 (2)
38분
0%
수강 전
92
[23회차]27. 면역계 - (8)T세포 성숙과 세포성 면역, T세포 선택과정 p.289
95분
0%
수강 전
93
[24회차]27 면역계 -적아세포증 p.292
86분
0%
수강 전
94
[24회차]28 호흡계 -(4)폐 p.312 (1)
39분
0%
수강 전
95
[24회차]28 호흡계 -(4)폐 p.312 (2)
65분
0%
수강 전
96
[24회차]28 호흡계 -(4)호흡량측정 p.319
64분
0%
수강 전
97
[25회차]29 소화와 영양 - ①섭취물의 이용 p.336
89분
0%
수강 전
98
[25회차]29 소화와 영양 - ⑥십이지장 p.345 (1)
56분
0%
수강 전
99
[25회차]29 소화와 영양 - ⑥십이지장 p.345 (2)
41분
0%
수강 전
100
[25회차]30 배설계 - ②신우와 수뇨관 p.366
73분
0%
수강 전
101
[26회차]30.배설계 (2)신장의 기능 ②재흡수와 분비 (ii)분비 그림30.14 p.369
82분
0%
수강 전
102
[26회차]31.체온조절 (2)내온동물(주로 항온동물) 그림31.04 p.390 (1)
42분
0%
수강 전
103
[26회차]31.체온조절 (2)내온동물(주로 항온동물) 그림31.04 p.390 (2)
51분
0%
수강 전
104
[26회차]32.식물학 (1)기관 ②줄기 (ii)줄기의 내부구조 그림32.08 p.402
74분
0%
수강 전
105
[27회차]32.식물학-수정-수술까지 p.407
94분
0%
수강 전
106
[27회차]32.식물학-(3) 물관,체관의 이동 p.415(1)
35분
0%
수강 전
107
[27회차]32.식물학-(3) 물관,체관의 이동 p.415(2)
51분
0%
수강 전
108
[27회차]32.식물학-브라시노스테로이드 호르몬 p.421
74분
0%
수강 전
109
[28회차]32. 식물학 - *광중단의 영향* p.424
97분
0%
수강 전
110
[28회차](3)계통분류학 - 자매군까지 p.443 (1)
45분
0%
수강 전
111
[28회차](3)계통분류학 - 자매군까지 p.443 (2)
45분
0%
수강 전
112
[28회차]집단유전학 p.448
87분
0%
수강 전
113
[29회차]34분류 - 생물들유연관계 p.467
92분
0%
수강 전
114
[29회차]34- ⑦원시 색소체 생물 p.472 (1)
14분
0%
수강 전
115
[29회차]34- ⑦원시 색소체 생물 p.472 (2)
39분
0%
수강 전
116
[29회차]34분류. ④속씨식물-표까지 p.480
72분
0%
수강 전
117
[30회차]34. 분류 - (4)동물 p.488
68분
0%
수강 전
118
[30회차]34. 분류 - (2)프리온 p.499 (1)
46분
0%
수강 전
119
[30회차]34. 분류 - (2)프리온 p.499 (2)
45분
0%
수강 전
120
[30회차]35. 생태학 - ②이타주의 p.515
48분
0%
수강 전
121
[31회차]35 생태학 -(4)개체군 성장유형 p.519
71분
0%
수강 전
122
[31회차]35 생태학 -(4)천이 p.527
97분
0%
수강 전
123
[32회차]생태계 - (3)에너지와 생태계 ①1차생산자 p.531
85분
0%
수강 전
124
[32회차]생태계 끝까지 p.539 끝까지 (완강)
91분
0%
수강 전
