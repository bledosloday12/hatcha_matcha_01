"""Emit aster_edge/index.html with deterministic layout bulk."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "index.html"

SPECIES = [
    ("EmberPeep", 11, 9, 10, 1),
    ("AquaCluck", 9, 11, 10, 2),
    ("LeafWing", 10, 10, 11, 3),
    ("SparkHen", 12, 8, 11, 4),
    ("FrostBrood", 8, 12, 9, 5),
    ("StoneRoost", 10, 13, 7, 6),
    ("GalePullet", 11, 8, 12, 1),
    ("ShadowCoop", 13, 9, 9, 7),
    ("SunComb", 10, 10, 10, 1),
    ("MoonBrooder", 9, 12, 10, 7),
    ("ThunderPeck", 14, 8, 10, 4),
    ("MossRunner", 9, 10, 12, 3),
    ("CrystalHen", 10, 11, 10, 8),
    ("MagmaWattle", 13, 9, 8, 1),
    ("TideCaller", 8, 11, 11, 2),
    ("BrambleBeak", 11, 10, 9, 3),
    ("VoltNest", 12, 9, 11, 4),
    ("GlacierLayer", 8, 13, 9, 5),
    ("QuartzCluck", 10, 12, 9, 8),
    ("DustDevil", 11, 9, 11, 6),
    ("StarlingChick", 9, 9, 13, 7),
    ("CometCrest", 12, 10, 9, 1),
    ("NebulaYolk", 10, 9, 12, 7),
    ("IonPeep", 13, 8, 11, 4),
    ("RootGuard", 9, 13, 9, 3),
    ("SiltStrider", 10, 10, 11, 6),
    ("BrineFang", 8, 10, 13, 2),
    ("CinderCrown", 14, 9, 8, 1),
    ("ZephyrDown", 9, 8, 14, 1),
    ("RuneRooster", 11, 11, 9, 8),
    ("EchoWing", 10, 9, 11, 7),
    ("PulseHen", 12, 10, 10, 4),
    ("FernShield", 8, 14, 9, 3),
    ("BasaltBeak", 11, 12, 8, 6),
    ("MirageLayer", 10, 9, 12, 7),
    ("TundraTalons", 9, 12, 10, 5),
    ("SolarFlare", 15, 8, 9, 1),
    ("AbyssalCluck", 9, 11, 11, 2),
    ("VerdantStrike", 11, 9, 11, 3),
    ("StormCrest", 13, 9, 10, 4),
    ("ObsidianBrood", 10, 13, 8, 6),
    ("LumenPeep", 9, 10, 12, 8),
    ("DuskRunner", 12, 9, 10, 7),
    ("GaleShard", 11, 10, 10, 4),
    ("MarshWarden", 9, 12, 10, 3),
    ("CoralCaller", 8, 11, 12, 2),
    ("EmberVault", 12, 11, 8, 1),
    ("IronFeather", 10, 14, 7, 6),
    ("VoidYolk", 13, 8, 11, 7),
]

MOVE_NAMES = [
    (1, "Peck Flick"),
    (2, "Dust Up"),
    (3, "Wing Buffer"),
    (4, "Seed Toss"),
    (5, "Beak Glint"),
    (6, "Cluck Pulse"),
    (7, "Strut Bash"),
    (8, "Spark Line"),
    (9, "Puddle Hop"),
    (10, "Static Down"),
    (11, "Barn Sweep"),
    (12, "Haymaker"),
    (13, "Drift Peck"),
    (14, "Gust Turn"),
    (15, "Stone Stomp"),
    (16, "Frost Ruffle"),
    (17, "Moss Wrap"),
    (18, "Tide Slap"),
    (19, "Shadow Dart"),
    (20, "Sun Flare"),
    (21, "Moon Hook"),
    (22, "Combo Rush"),
    (23, "Guarded Peck"),
    (24, "Tempo Swap"),
    (25, "Counter Coop"),
    (26, "League Finale"),
    (27, "Yolk Surge"),
    (28, "Crest Spin"),
    (29, "Brood Wall"),
    (30, "Arena Echo"),
    (31, "Vault Strike"),
    (32, "Void Tap"),
]

COACHING_TIPS = [
    "Bank grain before tournament weeks so training never stalls mid-bracket.",
    "Swap move slots after every evolution to cover new elemental spreads.",
    "Lead with tempo-heavy chicks when the opponent stacks guard.",
    "If you see frost-heavy benches, bring spark-line attackers with backup aqua coverage.",
    "Shadow broods punish careless spark spam — pack crystal finishers for late rounds.",
    "Stone roost lines love long stalls; break them with plant tempo flips.",
    "Keep at least one neutral-power bird to soak bad type matchups in blind picks.",
    "When leveling slows near 40, pivot to spar XP instead of pure forage loops.",
    "Rename birds early so JSON exports stay human-readable in guild tools.",
    "Use the entropy box to reproduce spars when filing bug reports against sims.",
    "Export roster JSON before browser refreshes; localStorage is intentionally unused here.",
    "Train might on glass cannons, guard on anchors, tempo on sweepers — not uniformly.",
    "Watch streak counters: they are morale proxies in this league flavor.",
    "If vitality lags, simulate feeding bursts before running five blitz spars.",
    "Crystal-type crest moves swing mirror matches — slot one per team.",
    "Moon brooders love night buffs in the Python trainer; on-chain ignores diurnal fluff.",
    "Avoid relying on miner bias — mainnet entropy differs from browser PRNG mocks.",
    "League pot donations on-chain require value; this page never sends ETH by itself.",
    "ADDRESS hints in the header mirror immutables baked into ChickCombo's constructor.",
    "Rotate species IDs in scrims to learn the full almanac, not just comfort picks.",
    "Use CSV exports when sharing lineups with non-technical coaches.",
    "If imports fail, validate JSON braces and trainer field first.",
    "Blitz mode is a stress test; pause if logs grow unreadable.",
    "Keep defender tempo high when facing might-heavy sweepers.",
    "Pack at least one low-base-might bird with huge grain income for economy games.",
    "Spar cooldown awareness saves gas grief on real settlements later.",
    "Evolution gates are strict: level 18 plus 900 XP before evolving.",
    "Move codes above 32 are rejected on-chain; keep slots honest.",
    "When testing type charts, cross-check lattice table against your mental model.",
    "Shadow > nothing is false — shadow participates in a tight triangle like others.",
    "Use matchup prediction helpers before committing to mint transactions.",
    "If roster diversity score is low, hatch missing elements before ranked play.",
    "Bench clears are destructive; export first.",
    "Power score heuristic here is might*2+guard+tempo — not identical to chain internals.",
    "Browser crypto entropy is adequate for UI drills, not for custody games.",
    "If animations stutter, reduce flakes by editing initFx density in source.",
    "League tag constants differ from other contracts — do not reuse salts elsewhere.",
    "Grain floor drills help you understand train_until loops in the Python app.",
    "When sparring, attacker might plus half tempo models aggressive pacing.",
    "Defender guard plus third tempo rewards stonewall builds.",
    "Type advantage adds a flat swing — enough to flip close rolls.",
    "XP gains on wins exceed losses; still farm responsibly.",
    "Nickname collisions are warnings in Python; rename to stay organized.",
    "Use scouting reports before merges when combining trainer JSON files.",
    "If you fork the UI, restyle tokens but keep accessibility contrast high.",
    "Keyboard users: tab across selects before hitting spar for predictable order.",
    "Screen readers: battle log is plain text; avoid relying on color alone.",
    "Void yolk species hits hard; respect its element when sideboarding.",
    "Iron feather skews guard — excellent into mixed assault teams.",
    "Coral callers love aqua tempo — test them against frost anchors.",
    "Marsh wardens stabilize plant lines with thick guard buffers.",
    "Gale shard spreads electric tempo without dumping guard completely.",
    "Dusk runners are shadow-streaked; bring crystal answers.",
    "Lumen peeps shine in crystal mirrors; pack diversity.",
    "Obsidian brood stonewalls; break with sustained might pressure.",
    "Storm crest offers spark consistency; watch water counters.",
    "Verdant strike is the plant tempo answer to brawlers.",
    "Abyssal cluck balances aqua bulk and tempo — great flex slot.",
    "Solar flare hits like a truck; keep grain to recover after spars.",
    "Tundra talons exemplify frost pacing — bait sparks carefully.",
    "Mirage layers blur tempo — expect swingy RNG bands.",
    "Basalt beak is the rock wall — pivot to grass if stalled.",
    "Fern shield is the plant tank — chip with fire safely.",
    "Pulse hen is the reliable spark sweeper — respect ground metaphors as stone checks.",
    "Echo wing plays shadow games — watch crystal crossfire.",
    "Rune rooster is crystal tech — learn its matchups early.",
    "Zephyr down chases speed — don't let it dictate tempo unchecked.",
    "Cinder crown is a fire cannon — water discipline required.",
    "Brinefang skews water speed — shock it with plant tempo if possible.",
    "Silt strider is the balanced earth flex — great third slot.",
    "Root guard is the plant wall — convert spikes into grain advantage.",
    "Ion peep plays electric tempo — frost partners help cover.",
    "Nebula yolk is shadow-fast — crystal coverage mandatory.",
    "Comet crest is a fire all-rounder — respect water anchors.",
    "Starling chick is the speedy shadow bird — don't chase blindly.",
    "Dust devil is wild earth tempo — expect RNG swings.",
    "Quartz cluck is crystal-guarded — break with shadow pressure if needed.",
    "Glacier layer is frost defense — spark breaks it clean.",
    "Volt nest is spark tempo — bring frost insurance.",
    "Bramble beak is plant offense — fire answers win.",
    "Tide caller is water balanced — grass tempo punishes laziness.",
    "Magma wattle is fire burst — aqua discipline wins.",
    "Crystal hen is the crystal anchor — diversify threats.",
    "Moss runner is plant speed — fire checks required.",
    "Thunder peck is electric offense — frost tanks help.",
    "Moon brooder is shadow bulk — crystal pierce matters.",
    "Sun comb is neutral fire tone — flex picks enjoy it.",
    "Shadow coop hits hard — crystal cross is mandatory.",
    "Gale pullet is air-flavored fire tempo — stone walls help in metaphor.",
    "Stone roost is the rock tank — grass breaks it.",
    "Frost brood stalls — spark breaks ice lines.",
    "Spark hen is electric might — respect frost partners.",
    "Leaf wing is plant tempo — fire discipline.",
    "Aqua cluck is water guard — grass tempo converts.",
    "Ember peep is the starter fire — learn triangles with it.",
]

ARENA_RULES = [
    "Gate A: hatch only when species catalog entry is non-zero on-chain.",
    "Gate B: rename collisions are allowed off-chain but discouraged for exports.",
    "Gate C: spar tickets reference attacker/defender ids; never reuse settled ids.",
    "Gate D: league pot accounting uses uint128 — watch sweep bounds in production.",
    "Gate E: donate path is nonReentrant; do not wrap with untrusted hooks.",
    "Gate F: ownership handoff is two-step; verify pending owner before accept.",
    "Gate G: pause is owner-only; publish incident runbooks referencing event CC_PauseSet.",
    "Gate H: ADDRESS_A may grant bonus grain — treat as privileged oracle, not user.",
    "Gate I: immutables are constructor-fixed; rotate by redeploying with new bytecode.",
    "Gate J: receive/fallback reject ETH — users must use donateLeague for value.",
    "Gate K: mint paths are nonReentrant to guard against weird ERC777 reentry (none here).",
    "Gate L: training picks mix SALT_A with prevrandao — casual entropy only.",
    "Gate M: forage mixes SALT_B with block number surrogate in Python, not on-chain.",
    "Gate N: evolve checks duplicate evolution via bool flag — cannot re-evolve.",
    "Gate O: move slots bounded to CC_MOVE_SLOTS — UI should clamp before send.",
    "Gate P: cooldown errors include timestamps — surface them in wallets.",
    "Gate Q: type chart is pure function — mirror in multiple clients for consensus.",
    "Gate R: streak mapping resets on loss — reflect in UI badges.",
    "Gate S: xp curve divisor 220 matches UI syncLevel — keep constants aligned.",
    "Gate T: level cap 72 is public constant — display in marketing footers.",
    "Gate U: species count 49 in this deployment — mint range checks must match.",
    "Gate V: grain spends on feed divide by three — UI can preview vitality bump.",
    "Gate V2: CC_LEAGUE_TAG is a fingerprint constant for integrators.",
    "Gate W: CC_SEASON_ID helps subgraph filters — emit with external metadata.",
    "Gate X: spar settlement grants xp only to winner — no pity XP on-chain.",
    "Gate Y: openSpar mapping grows — consider pruning pattern off-chain archival.",
    "Gate Z: ADDRESS_B/C reserved for future league modules — do not hardwire behavior yet.",
    "Appendix 1: browser sim uses PRNG; chain uses prevrandao — expect divergence.",
    "Appendix 2: export CSV quoting uses JSON.stringify on nicknames for commas safety.",
    "Appendix 3: blitz mode can deselect invalid pairs — always pick fresh bench slots.",
    "Appendix 4: coaching playbook references species by name — regenerate if catalog shifts.",
    "Appendix 5: advantage lattice colors are informational — not accessible alone.",
    "Appendix 6: combine chikn_LIKN digest exports with UI JSON for full snapshots.",
    "Appendix 7: selftest env flag is dev-only — strip from production automation.",
    "Appendix 8: move catalog codes align with MOVE_NAMES mapping in JS and Python.",
    "Appendix 9: training id input uses numeric field — validate parseInt NaN cases.",
    "Appendix 10: entropy textarea accepts partial hex — mixed with crypto randoms.",
]

DOUBLES_SYNERGY = [
    "EmberPeep + TideCaller: classic fire/water flex — bait plants then flip tempo.",
    "LeafWing + StormCrest: plant + spark covers frost stalls with offensive tempo.",
    "ShadowCoop + LumenPeep: shadow/crystal shell — punishes mirror greed.",
    "StoneRoost + ZephyrDown: rock/wind theme — guard anchors speedster pivots.",
    "FrostBrood + MagmaWattle: frost/fire tension — use as mindgames in blind picks.",
    "IonPeep + GlacierLayer: spark/frost lane — strong into aqua-heavy ladders.",
    "QuartzCluck + VoidYolk: crystal/shadow burst — fragile but explosive.",
    "IronFeather + MarshWarden: steel-plant vibe — outlasts mixed brawlers.",
    "CoralCaller + BrambleBeak: water/plant sustain — chip teams down slowly.",
    "SolarFlare + DuskRunner: day/night narrative — element coverage for fun scrims.",
]


def type_advantage_py(atk_elem: int, def_elem: int) -> int:
    if atk_elem == def_elem:
        return 0
    rings = ((1, 3, 2), (4, 2, 5), (6, 4, 7), (8, 7, 1))
    for a, b, c in rings:
        if atk_elem == a and def_elem == b:
            return 1
        if atk_elem == b and def_elem == c:
            return 1
        if atk_elem == c and def_elem == a:
            return 1
        if def_elem == a and atk_elem == b:
            return -1
        if def_elem == b and atk_elem == c:
            return -1
        if def_elem == c and atk_elem == a:
            return -1
    return 0


def main() -> None:
    lines: list[str] = []
    L = lines.append
    L("<!DOCTYPE html>")
    L('<html lang="en">')
    L("<head>")
    L('  <meta charset="utf-8" />')
    L('  <meta name="viewport" content="width=device-width, initial-scale=1" />')
    L("  <title>aster_edge — ChickCombo console</title>")
    L("  <style>")
    L("    :root {")
    L("      --bg0:#0c0f14;")
    L("      --bg1:#121826;")
    L("      --ink:#e8f0ff;")
    L("      --muted:#9fb2d7;")
    L("      --accent:#f7c948;")
    L("      --fire:#ff7a45;")
    L("      --aqua:#4cc9f0;")
    L("      --plant:#8fffba;")
    L("      --spark:#ffd447;")
    L("      --frost:#9bd6ff;")
    L("      --stone:#c7b8ff;")
    L("      --shadow:#b892ff;")
    L("      --crystal:#ffe0f7;")
    L("      --card:#1b2233;")
    L("      --line:#2a334a;")
    L("    }")
    L("    * { box-sizing: border-box; }")
    L("    body {")
    L("      margin:0;")
    L("      font-family: ui-sans-serif, system-ui, Segoe UI, Roboto, Helvetica, Arial;")
    L("      color: var(--ink);")
    L("      background: radial-gradient(1200px 800px at 20% 0%, #1a2140 0%, var(--bg0) 55%);")
    L("      min-height: 100vh;")
    L("    }")
    L("    header {")
    L("      padding: 28px clamp(16px, 4vw, 48px);")
    L("      border-bottom: 1px solid var(--line);")
    L("      background: linear-gradient(90deg, rgba(247,201,72,0.12), transparent);")
    L("    }")
    L("    header h1 { margin:0 0 8px; font-size: clamp(26px, 4vw, 40px); letter-spacing: 0.04em; }")
    L("    header p { margin:0; color: var(--muted); max-width: 900px; line-height: 1.5; }")
    L("    .wrap { padding: 24px clamp(16px, 4vw, 48px) 80px; display: grid; gap: 22px; }")
    L("    .grid { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }")
    L("    .card {")
    L("      background: linear-gradient(180deg, rgba(27,34,51,0.95), rgba(15,18,28,0.95));")
    L("      border: 1px solid var(--line);")
    L("      border-radius: 16px;")
    L("      padding: 16px;")
    L("      box-shadow: 0 18px 40px rgba(0,0,0,0.35);")
    L("    }")
    L("    .card h2 { margin: 0 0 12px; font-size: 18px; color: var(--accent); }")
    L("    label { display:block; font-size: 12px; color: var(--muted); margin: 8px 0 4px; }")
    L("    input, select, button, textarea {")
    L("      width: 100%;")
    L("      padding: 10px 12px;")
    L("      border-radius: 10px;")
    L("      border: 1px solid var(--line);")
    L("      background: #0f1420;")
    L("      color: var(--ink);")
    L("    }")
    L("    button { cursor: pointer; font-weight: 600; border: 1px solid rgba(247,201,72,0.35); }")
    L("    button.primary { background: linear-gradient(90deg, #f7c948, #ffb703); color:#1a1203; }")
    L("    button.ghost { background: transparent; color: var(--ink); }")
    L("    .row { display:flex; gap:10px; flex-wrap:wrap; }")
    L("    .row > * { flex: 1 1 160px; }")
    L("    .log {")
    L("      min-height: 180px;")
    L("      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;")
    L("      font-size: 12px;")
    L("      line-height: 1.45;")
    L("      white-space: pre-wrap;")
    L("    }")
    L("    table { width:100%; border-collapse: collapse; font-size: 12px; }")
    L("    th, td { border-bottom: 1px solid var(--line); padding: 8px 6px; text-align:left; }")
    L("    th { color: var(--muted); font-weight: 600; }")
    L("    .pill {")
    L("      display:inline-flex; align-items:center; gap:6px;")
    L("      padding: 4px 10px; border-radius: 999px;")
    L("      border:1px solid var(--line); background:#121826; font-size:12px; color: var(--muted);")
    L("    }")
    L("    .elem1{color:var(--fire)} .elem2{color:var(--aqua)} .elem3{color:var(--plant)}")
    L("    .elem4{color:var(--spark)} .elem5{color:var(--frost)} .elem6{color:var(--stone)}")
    L("    .elem7{color:var(--shadow)} .elem8{color:var(--crystal)}")
    L("    canvas#fx { position: fixed; inset: 0; pointer-events: none; z-index: 0; opacity: 0.35; }")
    L("    .above { position: relative; z-index: 1; }")
    L("    footer { padding: 24px; color: var(--muted); font-size: 12px; text-align:center; border-top:1px solid var(--line); }")
    L("    a { color: var(--accent); }")
    L("    .tip { color: var(--muted); font-size: 13px; line-height: 1.55; margin: 8px 0; }")
    L("    .kbd { font-family: ui-monospace, monospace; border:1px solid var(--line); padding:2px 6px; border-radius:6px; background:#0f1420; }")
    L("    .cols { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap: 12px; }")
    L("    .pos { color: #7CFFB2; font-weight: 700; }")
    L("    .neg { color: #FF7A7A; font-weight: 700; }")
    L("    .zero { color: var(--muted); }")
    L("    .micro { font-size: 11px; color: var(--muted); }")
    L("    .hero { font-size: 15px; color: var(--ink); margin-top: 6px; }")
    L("    .split { height:1px; background: var(--line); margin: 14px 0; }")
    L("  </style>")
    L("</head>")
    L("<body>")
    L('  <canvas id="fx" aria-hidden="true"></canvas>')
    L('  <div class="above">')
    L("    <header>")
    L('      <h1>aster_edge</h1>')
    L("      <p>")
    L("        Barnyard battle console themed like a pocket-monster league desk. Pair species, stage mock spars,")
    L("        and read type skew before you ship calldata to ChickCombo. Purely client-side — connect wallets only")
    L("        when you paste a real RPC yourself.")
    L("      </p>")
    L('      <p class="pill">Hints: 0x1D99cb8e9c62f38d4375f3c2Db0AA86c7B478552 · 0xe506D840582E64cA633d92317dD18DDEE790247D · 0x4Aa63867906B2370Ebb1068f7955fe579327BcE5</p>')
    L("    </header>")
    L('    <main class="wrap">')
    L('      <section class="grid">')
    L('        <div class="card">')
    L("          <h2>Roster lab</h2>")
    L('          <label for="nick">Trainer callsign</label>')
    L('          <input id="nick" autocomplete="off" value="EdgeCoach" />')
    L('          <label for="species">Hatch species</label>')
    L('          <select id="species"></select>')
    L('          <label for="name">Chick nickname</label>')
    L('          <input id="name" autocomplete="off" value="Peckachu" />')
    L('          <div class="row" style="margin-top:12px;">')
    L('            <button class="primary" id="btnHatch" type="button">Hatch to bench</button>')
    L('            <button class="ghost" id="btnClear" type="button">Clear bench</button>')
    L("          </div>")
    L('          <label for="trainId">Train chick id</label>')
    L('          <input id="trainId" inputmode="numeric" value="1" />')
    L('          <div class="row" style="margin-top:10px;">')
    L('            <button class="ghost" id="btnTrain" type="button">Train (−6 grain)</button>')
    L('            <button class="ghost" id="btnForage" type="button">Forage</button>')
    L("          </div>")
    L("        </div>")
    L('        <div class="card">')
    L("          <h2>Spar simulator</h2>")
    L('          <label for="left">Attacker slot</label>')
    L('          <select id="left"></select>')
    L('          <label for="right">Defender slot</label>')
    L('          <select id="right"></select>')
    L('          <div class="row" style="margin-top:12px;">')
    L('            <button class="primary" id="btnSpar" type="button">Run spar</button>')
    L('            <button class="ghost" id="btnBlitz" type="button">Blitz 5x</button>')
    L("          </div>")
    L('          <label for="entropy">Entropy hex (optional)</label>')
