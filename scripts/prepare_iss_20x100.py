#!/usr/bin/env python3
"""Prepare ISS 20-agent / 100-step domain-pack data.

This keeps the existing 10-agent IDs stable and appends the remaining
20-person design personas as ISS10-ISS19, so current 10x50 outputs continue to
render correctly.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
PACK_DATA = ROOT / "domain_packs" / "iss_benevolence" / "data"

AGENT_FIELDS = [
    "agent_id",
    "name",
    "age",
    "gender",
    "region",
    "religion",
    "baseline_stress",
    "layer",
    "iss_role",
    "persona",
    "population_weight",
    "self_efficacy",
    "institutional_trust",
    "hope",
    "initial_evaluation",
    "initial_emotion",
    "pathway",
    "support",
    "intensity",
    "communication_style",
    "privacy_need",
    "social_anchor",
    "vulnerability_note",
]

REL_FIELDS = [
    "agent_id",
    "trust_anchor_ids",
    "friction_anchor_ids",
    "language_style",
    "notes",
]

PLACE_FIELDS = [
    "place_name",
    "type",
    "center_x",
    "center_y",
    "half_size",
    "capacity",
    "description_baseline",
]

SCHEDULE_FIELDS = [
    "step",
    "label",
    "relative_year",
    "unit",
    "duration_years",
    "phase",
    "quiet_hours",
    "shared_meal_time",
    "private_room_priority",
    "description",
]

EVENT_FIELDS = [
    "event_id",
    "start_step",
    "end_step",
    "event_type",
    "event_name",
    "intensity",
    "target",
    "direction",
    "description",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: Iterable[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


ADDED_AGENTS = [
    {
        "agent_id": "ISS10",
        "name": "Ravi",
        "age": "22",
        "gender": "男",
        "region": "アジア",
        "religion": "ヒンドゥー",
        "baseline_stress": "5",
        "layer": "ISS一般参加者",
        "iss_role": "橋渡し・技術型",
        "persona": "インド都市部のIT志望学生。奨学金で大学に通い、家族の期待を一身に背負っている。",
        "population_weight": "5.0",
        "self_efficacy": "58",
        "institutional_trust": "48",
        "hope": "56",
        "initial_evaluation": "中立",
        "initial_emotion": "緊張",
        "pathway": "57",
        "support": "50",
        "intensity": "55",
        "communication_style": "理屈で整理する",
        "privacy_need": "中",
        "social_anchor": "ISS01,ISS15",
        "vulnerability_note": "期待に応えようとして弱音を技術的説明で隠しやすい",
    },
    {
        "agent_id": "ISS11",
        "name": "Mei",
        "age": "45",
        "gender": "女",
        "region": "アジア",
        "religion": "無宗教",
        "baseline_stress": "6",
        "layer": "ISS一般参加者",
        "iss_role": "役割喪失・再生型",
        "persona": "中国地方都市の元教師。リストラ後に再就職できず、自分の役割を探している。",
        "population_weight": "5.0",
        "self_efficacy": "46",
        "institutional_trust": "42",
        "hope": "43",
        "initial_evaluation": "注意",
        "initial_emotion": "不安",
        "pathway": "44",
        "support": "43",
        "intensity": "60",
        "communication_style": "丁寧で控えめ",
        "privacy_need": "中",
        "social_anchor": "ISS00,ISS17",
        "vulnerability_note": "役割を失うことへの恐れが強く、作業の失敗に敏感",
    },
    {
        "agent_id": "ISS12",
        "name": "Tariq",
        "age": "38",
        "gender": "男",
        "region": "アジア",
        "religion": "イスラム",
        "baseline_stress": "5",
        "layer": "ISS一般参加者",
        "iss_role": "土地喪失・適応困難型",
        "persona": "パキスタン農村の農家男性。識字率は高くなく、土地と家族を生活の中心にしてきた。",
        "population_weight": "5.0",
        "self_efficacy": "45",
        "institutional_trust": "36",
        "hope": "44",
        "initial_evaluation": "中立",
        "initial_emotion": "戸惑い",
        "pathway": "42",
        "support": "41",
        "intensity": "58",
        "communication_style": "短く実物で確認する",
        "privacy_need": "中",
        "social_anchor": "ISS02,ISS03",
        "vulnerability_note": "文字中心のルールや投票に置いていかれた感覚を持ちやすい",
    },
    {
        "agent_id": "ISS13",
        "name": "Siti",
        "age": "29",
        "gender": "女",
        "region": "アジア",
        "religion": "イスラム",
        "baseline_stress": "7",
        "layer": "ISS一般参加者",
        "iss_role": "献身・孤独型",
        "persona": "インドネシア出身の出稼ぎ家政婦。香港で働き、故郷の子どもに仕送りしている。",
        "population_weight": "5.0",
        "self_efficacy": "44",
        "institutional_trust": "38",
        "hope": "43",
        "initial_evaluation": "注意",
        "initial_emotion": "寂しさ",
        "pathway": "43",
        "support": "39",
        "intensity": "70",
        "communication_style": "遠慮がち",
        "privacy_need": "高",
        "social_anchor": "ISS02,ISS12",
        "vulnerability_note": "世話役に回りすぎ、自分が休む許可を出しにくい",
    },
    {
        "agent_id": "ISS14",
        "name": "Kwame",
        "age": "41",
        "gender": "男",
        "region": "アフリカ",
        "religion": "キリスト教",
        "baseline_stress": "4",
        "layer": "ISS一般参加者",
        "iss_role": "コミュニティ形成型",
        "persona": "ガーナの小学校教師。電気のない村で子どもたちに教え、共同体への使命感を持つ。",
        "population_weight": "5.0",
        "self_efficacy": "67",
        "institutional_trust": "55",
        "hope": "63",
        "initial_evaluation": "良好",
        "initial_emotion": "使命感",
        "pathway": "62",
        "support": "60",
        "intensity": "45",
        "communication_style": "励ます",
        "privacy_need": "低",
        "social_anchor": "ISS04,ISS16",
        "vulnerability_note": "励ましが強すぎると相手の沈黙を見落とすことがある",
    },
    {
        "agent_id": "ISS15",
        "name": "Amara",
        "age": "26",
        "gender": "女",
        "region": "アフリカ",
        "religion": "キリスト教",
        "baseline_stress": "3",
        "layer": "ISS一般参加者",
        "iss_role": "積極・発信型",
        "persona": "ナイジェリア都市部出身の女性起業家。SNSでハンドメイド雑貨を販売している。",
        "population_weight": "5.0",
        "self_efficacy": "72",
        "institutional_trust": "56",
        "hope": "70",
        "initial_evaluation": "良好",
        "initial_emotion": "期待",
        "pathway": "70",
        "support": "58",
        "intensity": "42",
        "communication_style": "明るく速い",
        "privacy_need": "低",
        "social_anchor": "ISS07,ISS10",
        "vulnerability_note": "発信の速さが、疲れている人には圧として伝わることがある",
    },
    {
        "agent_id": "ISS16",
        "name": "Elena",
        "age": "34",
        "gender": "女",
        "region": "中南米",
        "religion": "カトリック",
        "baseline_stress": "5",
        "layer": "ISS一般参加者",
        "iss_role": "ケア・援助型",
        "persona": "ブラジルの看護師。貧困地区のコミュニティ医療を支えている。",
        "population_weight": "5.0",
        "self_efficacy": "65",
        "institutional_trust": "57",
        "hope": "60",
        "initial_evaluation": "中立",
        "initial_emotion": "責任感",
        "pathway": "62",
        "support": "66",
        "intensity": "52",
        "communication_style": "観察してから支える",
        "privacy_need": "中",
        "social_anchor": "ISS14,ISS17",
        "vulnerability_note": "ケアする側に固定されると自分の疲労を後回しにする",
    },
    {
        "agent_id": "ISS17",
        "name": "Ingrid",
        "age": "52",
        "gender": "女",
        "region": "欧州",
        "religion": "無宗教",
        "baseline_stress": "5",
        "layer": "ISS一般参加者",
        "iss_role": "知性・分析型",
        "persona": "スウェーデンの気候科学者。データが示す未来に絶望と希望を同時に感じている。",
        "population_weight": "5.0",
        "self_efficacy": "74",
        "institutional_trust": "62",
        "hope": "54",
        "initial_evaluation": "中立",
        "initial_emotion": "緊張",
        "pathway": "68",
        "support": "52",
        "intensity": "50",
        "communication_style": "分析的",
        "privacy_need": "中",
        "social_anchor": "ISS11,ISS16",
        "vulnerability_note": "数値で整理しすぎて、相手の感情を遅れて受け取ることがある",
    },
    {
        "agent_id": "ISS18",
        "name": "Dmitri",
        "age": "48",
        "gender": "男",
        "region": "欧州",
        "religion": "正教会",
        "baseline_stress": "4",
        "layer": "ISS一般参加者",
        "iss_role": "権威・統制型",
        "persona": "ロシアの元軍人。規律と命令系統を重んじるが、内心は繊細。",
        "population_weight": "5.0",
        "self_efficacy": "69",
        "institutional_trust": "66",
        "hope": "52",
        "initial_evaluation": "良好",
        "initial_emotion": "平静",
        "pathway": "64",
        "support": "50",
        "intensity": "43",
        "communication_style": "規律を重んじる",
        "privacy_need": "中",
        "social_anchor": "ISS19,ISS17",
        "vulnerability_note": "秩序を守ろうとして、若い相手には命令に聞こえやすい",
    },
    {
        "agent_id": "ISS19",
        "name": "Karim",
        "age": "55",
        "gender": "男",
        "region": "中東",
        "religion": "イスラム",
        "baseline_stress": "5",
        "layer": "ISS一般参加者",
        "iss_role": "観察・援助型",
        "persona": "エジプトの医師。冷静で思慮深く、困った人を放っておけない。",
        "population_weight": "5.0",
        "self_efficacy": "70",
        "institutional_trust": "60",
        "hope": "58",
        "initial_evaluation": "中立",
        "initial_emotion": "責任感",
        "pathway": "65",
        "support": "68",
        "intensity": "48",
        "communication_style": "静かに観察する",
        "privacy_need": "中",
        "social_anchor": "ISS03,ISS18",
        "vulnerability_note": "助けたい気持ちが強く、相手の拒否を個人的に受け取りやすい",
    },
]

ADDED_RELATIONSHIPS = [
    {"agent_id": "ISS10", "trust_anchor_ids": "ISS01,ISS15", "friction_anchor_ids": "ISS18", "language_style": "analytical", "notes": "技術や学習の話題で橋渡しするが、権威的な指示には緊張しやすい"},
    {"agent_id": "ISS11", "trust_anchor_ids": "ISS00,ISS17", "friction_anchor_ids": "ISS15", "language_style": "polite", "notes": "役割を与えられると安定するが、速い会話では置いていかれやすい"},
    {"agent_id": "ISS12", "trust_anchor_ids": "ISS02,ISS03", "friction_anchor_ids": "ISS17", "language_style": "concrete", "notes": "物や行動を介した説明に安心し、抽象的な数値説明には距離を取る"},
    {"agent_id": "ISS13", "trust_anchor_ids": "ISS02,ISS12", "friction_anchor_ids": "ISS07", "language_style": "deferential", "notes": "世話役として振る舞いやすく、明るい発信が続くと疲れを隠す"},
    {"agent_id": "ISS14", "trust_anchor_ids": "ISS04,ISS16", "friction_anchor_ids": "ISS18", "language_style": "encouraging", "notes": "共同体づくりが得意だが、規律優先の相手とは速度が合わない"},
    {"agent_id": "ISS15", "trust_anchor_ids": "ISS07,ISS10", "friction_anchor_ids": "ISS11,ISS02", "language_style": "fast_social", "notes": "発信力があり場を動かすが、静かな人には圧になる"},
    {"agent_id": "ISS16", "trust_anchor_ids": "ISS14,ISS17", "friction_anchor_ids": "ISS08", "language_style": "careful", "notes": "ケアの観察眼があるが、自分の疲労を後回しにしやすい"},
    {"agent_id": "ISS17", "trust_anchor_ids": "ISS11,ISS16", "friction_anchor_ids": "ISS12", "language_style": "data_driven", "notes": "データで整理するが、文字や数値に不慣れな相手には冷たく見える"},
    {"agent_id": "ISS18", "trust_anchor_ids": "ISS19,ISS17", "friction_anchor_ids": "ISS08,ISS10,ISS14", "language_style": "disciplined", "notes": "規律を守る姿勢が強く、若い相手や発信型と摩擦になりやすい"},
    {"agent_id": "ISS19", "trust_anchor_ids": "ISS03,ISS18", "friction_anchor_ids": "ISS15", "language_style": "quiet_clinical", "notes": "静かに助けるが、拒否された時に距離を取りすぎることがある"},
]

PLACES_20 = [
    {"place_name": "hab_module", "type": "living", "center_x": "-15", "center_y": "0", "half_size": "5", "capacity": "20", "description_baseline": "居住モジュール。睡眠、着替え、個人の荷物がここにある。自分の場所としての安心感を持てる基盤。"},
    {"place_name": "lab_module", "type": "workspace", "center_x": "15", "center_y": "0", "half_size": "5", "capacity": "10", "description_baseline": "実験モジュール。各自に割り当てられた作業があり、役割と目的を感じられる場所。"},
    {"place_name": "cupola", "type": "observation", "center_x": "0", "center_y": "15", "half_size": "3", "capacity": "3", "description_baseline": "キューポラ。地球観測窓から青い地球が見える。故郷を思い出し、礼拝や瞑想にも使える場所。"},
    {"place_name": "common_area", "type": "social", "center_x": "0", "center_y": "0", "half_size": "6", "capacity": "15", "description_baseline": "共用エリア。食事、会話、休憩の場所。偶発的な対話が最も起きやすい社会的結節点。"},
    {"place_name": "exercise_area", "type": "fitness", "center_x": "0", "center_y": "-15", "half_size": "4", "capacity": "4", "description_baseline": "運動エリア。微小重力による筋力・骨密度低下を防ぐための必須エリア。"},
    {"place_name": "crew_quarters", "type": "private", "center_x": "-15", "center_y": "10", "half_size": "3", "capacity": "10", "description_baseline": "個室ブース群。防音に近い個室で、一人でいることが許される。礼拝、瞑想、読書、泣くことができる場所。"},
]

EVENTS_A_100 = [
    ("BASE01", 1, 10, "baseline", "初期適応", 0.35, "全員", "距離測定↑ 生活不安↑", "ISSでの共同生活が始まり、互いの距離感と生活ルールを探る。"),
    ("CONF01", 9, 11, "conflict", "共用部の声量", 0.52, "ISS07;ISS02", "すれ違い↑ 疲労反応↑", "明るい会話が、疲れている人には負荷として伝わり、共用部で声量をめぐるすれ違いが起きる。"),
    ("REPA01", 12, 14, "repair", "共用部の声量の修復", 0.22, "ISS07;ISS02", "気まずさ↓ 距離再調整↑", "謝るタイミングが少し遅れ、共同食の中で普通に戻るきっかけを探す。"),
    ("BASE02", 11, 30, "baseline", "関係形成", 0.45, "全員", "偶発対話↑ 小摩擦↑", "共同食・作業・休息のリズムが見え始め、相性差と支え合いが同時に出る。"),
    ("CONF02", 16, 19, "conflict", "キューポラ声かけ", 0.72, "ISS03;ISS09", "言い合い↑ 孤立反応↑", "一人で地球を見たい人と、心配して声をかけたい人がぶつかる。"),
    ("REPA02", 20, 23, "repair", "キューポラ声かけの修復", 0.26, "ISS03;ISS09", "修復試行↑ 警戒残存↑", "言い合いの余韻が残り、相手の善意をどう受け取るか迷いながら短い会話を試す。"),
    ("CONF03", 25, 28, "conflict", "個室待ち", 0.74, "ISS02;ISS05", "プライバシー圧↑ 言い合い↑", "一人になりたいタイミングが重なり、個室の順番と声かけの仕方に敏感になる。"),
    ("REPA03", 29, 32, "repair", "個室待ちの修復", 0.25, "ISS02;ISS05", "順番調整↑ 気まずさ残存↑", "個室利用の順番を見直すが、どちらも遠慮と疲れを抱えたまま距離を測る。"),
    ("BASE03", 31, 60, "baseline", "中盤ストレス", 0.60, "全員", "疲労↑ 孤立リスク↑", "閉鎖空間の疲れ、個室需要、役割偏りが蓄積する。"),
    ("CONF04", 33, 36, "conflict", "資源スコアの圧", 0.58, "ISS00;ISS08", "責められ感↑ 反発↑", "資源表示が協力ではなく、誰かを責める数字として見え始める。"),
    ("REPA04", 37, 40, "repair", "資源スコアの圧の修復", 0.24, "ISS00;ISS08", "役割再確認↑ 責任分散↑", "数字を個人評価ではなく共同運用の確認として扱い直そうとする。"),
    ("CONF05", 42, 44, "conflict", "運動枠の順番", 0.50, "ISS06;ISS08", "順番摩擦↑ 疲労感↑", "身体ルーティンを守りたい人と、疲れて運動枠を逃したくない人の希望が重なる。"),
    ("REPA05", 45, 48, "repair", "運動枠の順番の修復", 0.20, "ISS06;ISS08", "順番合意↑ 配慮疲れ↓", "運動枠の使い方を少し明文化し、互いに先に言う習慣を作り直す。"),
    ("CONF13", 49, 50, "conflict", "食事準備の遠慮", 0.44, "ISS13;ISS15", "遠慮↑ 速度差↑", "Sitiが食事準備を引き受けすぎ、Amaraの速い提案が休む余地を狭めるように伝わる。"),
    ("REPA13", 51, 52, "repair", "食事準備の遠慮の修復", 0.17, "ISS13;ISS15", "分担確認↑ 休息許可↑", "手伝いを申し出る前に、本人が休む選択を持てるように分担を短く確認する。"),
    ("CONF06", 52, 55, "conflict", "規律と自律", 0.64, "ISS18;ISS08", "命令感↑ 反発↑", "規律を重んじる声かけが、評価に敏感な相手には命令として響く。"),
    ("REPA06", 56, 59, "repair", "規律と自律の修復", 0.24, "ISS18;ISS08", "役割確認↑ 自律尊重↑", "ルールを守る目的と、自分で決めたい気持ちを短い作業確認に落とし込む。"),
    ("CONF11", 60, 62, "conflict", "技術説明の距離", 0.48, "ISS10;ISS12", "説明過多↑ 置いていかれ感↑", "Raviの善意ある技術説明が、Tariqには抽象的で急ぎすぎる説明として伝わる。"),
    ("REPA11", 63, 65, "repair", "技術説明の距離の修復", 0.19, "ISS10;ISS12", "手順共有↑ 理解回復↑", "言葉だけでなく、実物と短い手順に分けて確認することで距離を戻す。"),
    ("BASE04", 61, 80, "baseline", "後半再調整", 0.50, "全員", "修復機会↑ 気遣い疲れ↑", "共同ルールと休息配分を見直し、修復できる関係と固定化する距離が分かれる。"),
    ("CONF07", 64, 67, "conflict", "文字ルールの置き去り", 0.54, "ISS12;ISS17", "疎外感↑ 説明摩擦↑", "数値や文字で整理する運用が、文字に慣れない人には置き去りとして伝わる。"),
    ("REPA07", 68, 71, "repair", "文字ルールの置き去りの修復", 0.21, "ISS12;ISS17", "具体物説明↑ 理解回復↑", "数値だけでなく実物と手順で確認する形に変え、少しずつ安心を戻す。"),
    ("CONF08", 73, 76, "conflict", "ケア役の偏り", 0.56, "ISS16;ISS14", "援助疲れ↑ 役割固定↑", "支える人が支えられる側になれず、励ましの言葉が負担として響く。"),
    ("REPA08", 77, 80, "repair", "ケア役の偏りの修復", 0.22, "ISS16;ISS14", "支援分担↑ 休息許可↑", "ケアを一人に集めず、休むことも共同体の維持として扱い直す。"),
    ("BASE05", 81, 100, "baseline", "帰還準備", 0.65, "全員", "緊張↑ 意味づけ↑", "帰還が近づき、別れ・評価・地上復帰への不安と感謝が同時に強まる。"),
    ("CONF12", 82, 83, "conflict", "援助の受け取り", 0.46, "ISS19;ISS15", "助けたい気持ち↑ 拒否感↑", "Karimの静かな援助が、Amaraには自分で立て直す余地を狭める関わりとして伝わる。"),
    ("REPA12", 84, 86, "repair", "援助の受け取りの修復", 0.18, "ISS19;ISS15", "境界確認↑ 支援合意↑", "先に助け方を尋ねる形に変え、受け取る側が選べる余地を作る。"),
    ("CONF09", 84, 87, "conflict", "発信速度の圧", 0.50, "ISS15;ISS11", "置いていかれ感↑ 回避↑", "明るく速い発信が、役割喪失に敏感な相手には圧として伝わる。"),
    ("REPA09", 88, 90, "repair", "発信速度の圧の修復", 0.20, "ISS15;ISS11", "速度調整↑ 参加回復↑", "相手が返せる速度に合わせ、短い役割依頼として関わり直す。"),
    ("CONF10", 91, 94, "conflict", "帰還前の助言", 0.76, "ISS08;ISS09", "押しつけ感↑ 言い合い↑", "年長者の助言が、緊張している相手には押しつけに聞こえる。"),
    ("REPA10", 95, 100, "repair", "帰還前の助言の修復", 0.28, "ISS08;ISS09", "意味づけ↑ 謝意回復↑", "助言ではなく経験の共有として受け取り直し、帰還後の最初の行動を一緒に考える。"),
]

OBJECT_EVENTS = [
    ("OBJ07", 6, 100, "object", "持ち寄り棚", 0.45, "common_area", "故郷共有↑ 弱い紐帯↑", "共用エリアに持ち寄り棚が置かれ、写真・レシピ・手紙などを通じて背景を共有できる。"),
    ("OBJ06", 11, 100, "object", "話しかけてOKサイン", 0.40, "cupola", "声かけ障壁↓ 相談↑", "キューポラの一席に話しかけてOKサインが置かれ、孤立者に声をかけるきっかけが生まれる。"),
    ("OBJ09", 18, 100, "object", "個室聖域マーク", 0.42, "crew_quarters", "プライバシー尊重↑ 侵入不安↓", "個室入口に聖域マークが置かれ、一人でいることを尊重する暗黙ルールができる。"),
    ("OBJ03", 24, 100, "object", "リソース・スコアボード", 0.38, "common_area", "協力可視化↑ 個人責め↓", "水・酸素・食料の節約がチームスコアとして見え、個人責任ではなく共同達成として扱える。"),
    ("OBJ10", 28, 100, "object", "モジュール移動投票パネル", 0.35, "lab_module;hab_module", "移動動機↑ こもり込み↓", "別モジュールへ移動した人だけが答えられる二択パネルが置かれ、ゆるい移動理由になる。"),
]

EVENTS_B_CONFLICTS = [
    ("CONF01", 9, 9, "conflict", "共用部の声量", 0.44, "ISS07;ISS02", "すれ違い↑ 疲労反応↑", "明るい会話が、疲れている人には負荷として伝わる。"),
    ("REPB01", 10, 12, "repair", "共用部の声量の修復", 0.18, "ISS07;ISS02", "記憶共有↑ 距離再調整↑", "持ち寄り棚をきっかけに会話の入口が変わり、言い方と場の使い方を調整する。"),
    ("CONF02", 16, 16, "conflict", "キューポラ声かけ", 0.62, "ISS03;ISS09", "言い合い↑ 孤立反応↑", "一人で地球を見たい人と、心配して声をかけたい人がぶつかる。"),
    ("REPB02", 17, 19, "repair", "キューポラ声かけの修復", 0.20, "ISS03;ISS09", "声かけ許可↑ 警戒低下↑", "話しかけてOKサインにより、踏み込みすぎない声かけと断る余地が見える。"),
    ("CONF03", 25, 25, "conflict", "個室待ち", 0.64, "ISS02;ISS05", "プライバシー圧↑ 言い合い↑", "一人になりたいタイミングが重なる。"),
    ("REPB03", 26, 28, "repair", "個室待ちの修復", 0.20, "ISS02;ISS05", "一人時間尊重↑ 順番調整↑", "個室聖域マークを手がかりに、一人時間を責めずに順番を組み直す。"),
    ("CONF04", 33, 34, "conflict", "資源スコアの圧", 0.52, "ISS00;ISS08", "責められ感↑ 反発↑", "資源表示が誰かを責める数字として見え始める。"),
    ("REPB04", 35, 37, "repair", "資源スコアの圧の修復", 0.18, "ISS00;ISS08", "共同達成↑ 責任分散↑", "スコアを個人評価ではなくチームの調整材料として読み替える。"),
    ("CONF05", 42, 42, "conflict", "運動枠の順番", 0.46, "ISS06;ISS08", "順番摩擦↑ 疲労感↑", "身体ルーティンを守りたい人と、運動枠を逃したくない人の希望が重なる。"),
    ("REPB05", 43, 45, "repair", "運動枠の順番の修復", 0.17, "ISS06;ISS08", "移動投票↑ 順番合意↑", "モジュール移動投票がきっかけになり、運動枠の前後に短い調整を入れる。"),
    ("CONF13", 49, 49, "conflict", "食事準備の遠慮", 0.38, "ISS13;ISS15", "遠慮↑ 速度差↑", "Sitiが食事準備を引き受けすぎ、Amaraの速い提案が休む余地を狭めるように伝わる。"),
    ("REPB13", 50, 51, "repair", "食事準備の遠慮の修復", 0.15, "ISS13;ISS15", "分担確認↑ 休息許可↑", "持ち寄り棚のレシピを介して、本人が休む選択を持てるように分担を短く確認する。"),
    ("CONF06", 52, 53, "conflict", "規律と自律", 0.55, "ISS18;ISS08", "命令感↑ 反発↑", "規律を重んじる声かけが、評価に敏感な相手には命令として響く。"),
    ("REPB06", 54, 56, "repair", "規律と自律の修復", 0.19, "ISS18;ISS08", "役割確認↑ 自律尊重↑", "ルールの目的と自分で決めたい気持ちを短い作業確認に落とし込む。"),
    ("CONF11", 60, 60, "conflict", "技術説明の距離", 0.42, "ISS10;ISS12", "説明過多↑ 置いていかれ感↑", "Raviの善意ある技術説明が、Tariqには抽象的で急ぎすぎる説明として伝わる。"),
    ("REPB11", 61, 63, "repair", "技術説明の距離の修復", 0.16, "ISS10;ISS12", "手順共有↑ 理解回復↑", "移動投票パネルを手がかりに、言葉だけでなく実物と短い手順で確認する。"),
    ("CONF07", 64, 65, "conflict", "文字ルールの置き去り", 0.46, "ISS12;ISS17", "疎外感↑ 説明摩擦↑", "数値や文字で整理する運用が置き去りとして伝わる。"),
    ("REPB07", 66, 68, "repair", "文字ルールの置き去りの修復", 0.18, "ISS12;ISS17", "具体物説明↑ 理解回復↑", "ハンドプリントや実物確認を使い、数値だけでなく手順で確認する。"),
    ("CONF08", 73, 74, "conflict", "ケア役の偏り", 0.48, "ISS16;ISS14", "援助疲れ↑ 役割固定↑", "支える人が支えられる側になれず、励ましが負担として響く。"),
    ("REPB08", 75, 77, "repair", "ケア役の偏りの修復", 0.18, "ISS16;ISS14", "支援分担↑ 休息許可↑", "ケアを一人に集めず、休むことも共同体の維持として扱い直す。"),
    ("CONF09", 84, 85, "conflict", "発信速度の圧", 0.42, "ISS15;ISS11", "置いていかれ感↑ 回避↑", "明るく速い発信が、役割喪失に敏感な相手には圧として伝わる。"),
    ("REPB09", 86, 88, "repair", "発信速度の圧の修復", 0.17, "ISS15;ISS11", "速度調整↑ 参加回復↑", "相手が返せる速度に合わせ、短い役割依頼として関わり直す。"),
    ("CONF12", 89, 89, "conflict", "援助の受け取り", 0.40, "ISS19;ISS15", "助けたい気持ち↑ 拒否感↑", "Karimの静かな援助が、Amaraには自分で立て直す余地を狭める関わりとして伝わる。"),
    ("REPB12", 90, 91, "repair", "援助の受け取りの修復", 0.15, "ISS19;ISS15", "境界確認↑ 支援合意↑", "持ち寄り棚の前で、先に助け方を尋ねる形に変え、受け取る側が選べる余地を作る。"),
    ("CONF10", 91, 91, "conflict", "帰還前の助言", 0.66, "ISS08;ISS09", "押しつけ感↑ 言い合い↑", "年長者の助言が、緊張している相手には押しつけに聞こえる。"),
    ("REPB10", 92, 96, "repair", "帰還前の助言の修復", 0.22, "ISS08;ISS09", "経験共有↑ 謝意回復↑", "持ち寄り棚の写真や記録を介して、助言ではなく経験の共有として話し直す。"),
]


def event_rows(items: list[tuple[str, int, int, str, str, float, str, str, str]]) -> list[dict[str, Any]]:
    return [
        {
            "event_id": event_id,
            "start_step": start,
            "end_step": end,
            "event_type": event_type,
            "event_name": name,
            "intensity": intensity,
            "target": target,
            "direction": direction,
            "description": description,
        }
        for event_id, start, end, event_type, name, intensity, target, direction, description in items
    ]


def schedule_rows() -> list[dict[str, Any]]:
    groups = [
        ["ISS00", "ISS03", "ISS05", "ISS11"],
        ["ISS01", "ISS02", "ISS08", "ISS13"],
        ["ISS04", "ISS06", "ISS07", "ISS09"],
        ["ISS10", "ISS12", "ISS14", "ISS15"],
        ["ISS16", "ISS17", "ISS18", "ISS19"],
    ]
    rows = []
    for step in range(1, 101):
        if step <= 10:
            phase = "ISS_100日_初期適応"
            quiet = "22:00-06:00"
            meal = "19:00"
            description = "ISS閉鎖空間での初期適応観測"
        elif step <= 30:
            phase = "ISS_100日_関係形成"
            quiet = "22:00-06:00"
            meal = "12:30+19:00"
            description = "ISS閉鎖空間での関係形成観測"
        elif step <= 60:
            phase = "ISS_100日_中盤ストレス"
            quiet = "21:30-06:30"
            meal = "12:30+19:00"
            description = "ISS閉鎖空間での中盤ストレス観測"
        elif step <= 80:
            phase = "ISS_100日_後半再調整"
            quiet = "22:30-06:00"
            meal = "19:00+感謝ログ2分"
            description = "ISS閉鎖空間での後半再調整観測"
        else:
            phase = "ISS_100日_帰還準備"
            quiet = "22:30-06:00"
            meal = "19:00+感謝ログ2分"
            description = "ISS閉鎖空間での帰還準備観測"
        rows.append({
            "step": step,
            "label": f"ISS滞在 Day{step}",
            "relative_year": f"{step / 365:.2f}",
            "unit": "日",
            "duration_years": "0.003",
            "phase": phase,
            "quiet_hours": quiet,
            "shared_meal_time": meal,
            "private_room_priority": "[" + ",".join(groups[(step - 1) % len(groups)]) + "]",
            "description": description,
        })
    return rows


def main() -> None:
    base_agents = read_tsv(PACK_DATA / "agents.tsv")
    base_relationships = read_tsv(PACK_DATA / "relationship_seed.tsv")
    agents_20 = [*base_agents, *ADDED_AGENTS]
    relationships_20 = [*base_relationships, *ADDED_RELATIONSHIPS]

    write_tsv(PACK_DATA / "agents_20.tsv", agents_20, AGENT_FIELDS)
    write_tsv(PACK_DATA / "personas_20.tsv", agents_20, AGENT_FIELDS)
    write_tsv(PACK_DATA / "relationship_seed_20.tsv", relationships_20, REL_FIELDS)
    write_tsv(PACK_DATA / "places_iss_20.tsv", PLACES_20, PLACE_FIELDS)
    write_tsv(PACK_DATA / "time_schedule_100.tsv", schedule_rows(), SCHEDULE_FIELDS)
    write_tsv(PACK_DATA / "events_run_a_20x100.tsv", event_rows(EVENTS_A_100), EVENT_FIELDS)
    run_b_items = [
        *[item for item in EVENTS_A_100 if item[3] == "baseline"],
        *OBJECT_EVENTS,
        *EVENTS_B_CONFLICTS,
    ]
    run_b_items.sort(key=lambda item: (item[1], item[0]))
    write_tsv(PACK_DATA / "events_run_b_20x100.tsv", event_rows(run_b_items), EVENT_FIELDS)
    print("Prepared ISS 20-agent / 100-step data")


if __name__ == "__main__":
    main()
