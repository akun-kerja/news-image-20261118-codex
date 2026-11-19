from PIL import Image, ImageDraw, ImageFont
import math

W = H = 1024
PAPER = "#F3F0E8"
INK = "#172536"
MUTED = "#65717B"
RED = "#C63D32"
GOLD = "#D7A64A"
BLUE = "#274C6B"
WHITE = "#FFFDF8"

im = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(im)
regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
serif = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

def font(size, weight="regular"):
    return ImageFont.truetype({"regular": regular, "bold": bold, "serif": serif}[weight], size)

def text(x, y, s, size, fill=INK, weight="regular"):
    d.text((x, y), s, font=font(size, weight), fill=fill)

def wrap(s, f, width):
    lines, line = [], ""
    for word in s.split():
        candidate = (line + " " + word).strip()
        if d.textlength(candidate, font=f) <= width:
            line = candidate
        else:
            if line: lines.append(line)
            line = word
    if line: lines.append(line)
    return lines

def paragraph(x, y, s, size, width, fill=INK, leading=6, max_lines=None):
    f = font(size)
    lines = wrap(s, f, width)
    if max_lines: lines = lines[:max_lines]
    for i, line in enumerate(lines):
        text(x, y + i * (size + leading), line, size, fill)
    return y + len(lines) * (size + leading)

def card(x, y, w, h, tag, title, body, accent=BLUE, title_size=22):
    d.rounded_rectangle((x, y, x+w, y+h), radius=12, fill=WHITE, outline="#D9D5CA", width=2)
    d.rounded_rectangle((x, y, x+8, y+h), radius=4, fill=accent)
    text(x+24, y+16, tag.upper(), 13, accent, "bold")
    lines = wrap(title, font(title_size, "bold"), w-48)
    for i, line in enumerate(lines[:2]): text(x+24, y+40+i*(title_size+3), line, title_size, INK, "bold")
    by = y+44+len(lines[:2])*(title_size+3)
    paragraph(x+24, by, body, 16, w-48, MUTED, 4, 3)

# Masthead
d.rectangle((0, 0, W, 104), fill=INK)
text(34, 12, "THE WORLD LEDGER", 17, GOLD, "bold")
text(32, 35, "WORLD NEWS", 42, WHITE, "serif")
text(645, 25, "WEDNESDAY", 17, GOLD, "bold")
text(645, 48, "18 NOVEMBER 2026", 23, WHITE, "bold")
d.rectangle((0, 104, W, 112), fill=RED)

# Lead feature
d.rounded_rectangle((28, 130, 996, 452), radius=16, fill=INK)
text(54, 151, "ASIA-PACIFIC  •  SHENZHEN", 15, GOLD, "bold")
text(54, 184, "A SUMMIT THAT", 33, WHITE, "serif")
text(54, 222, "COULD RESHAPE", 33, WHITE, "serif")
text(54, 260, "THE WORLD", 33, WHITE, "serif")
d.rectangle((54, 310, 460, 313), fill=RED)
paragraph(54, 328, "Xi Jinping meets Vladimir Putin at APEC. Donald Trump joins them for a three-way summit on Thursday.", 19, 420, "#E2E5E7", 7, 4)
text(54, 416, "THE DAY'S LEAD STORY", 13, GOLD, "bold")

# Original geometric summit illustration: three figures around a globe
cx, cy = 758, 292
d.ellipse((617, 164, 940, 424), fill="#203B53", outline="#42627C", width=2)
# globe and longitude/latitude arcs
d.ellipse((701, 213, 855, 367), fill="#D9E4D8", outline=GOLD, width=4)
d.arc((727, 213, 829, 367), 70, 290, fill="#75938E", width=3)
d.arc((701, 246, 855, 334), 0, 360, fill="#75938E", width=2)
d.polygon([(705,282),(731,264),(748,271),(744,287),(730,295),(722,318),(708,310)], fill="#66856F")
d.polygon([(790,244),(824,255),(842,277),(825,289),(818,311),(801,306),(793,280),(777,267)], fill="#66856F")
# podiums and three stylized leaders
for px, color in [(656, RED), (757, GOLD), (858, "#91A9B7")]:
    d.rounded_rectangle((px, 341, px+70, 399), radius=7, fill=color)
    d.ellipse((px+20, 310, px+50, 344), fill="#D9B395")
    d.pieslice((px+14, 302, px+56, 327), 180, 360, fill="#33404B")
    d.rectangle((px+30, 322, px+40, 346), fill="#D9B395")
    d.line((px+34, 350, px+34, 387), fill=WHITE, width=3)
    d.line((px+20, 363, px+50, 363), fill=WHITE, width=3)
text(636, 405, "XI", 12, WHITE, "bold")
text(735, 405, "PUTIN", 12, WHITE, "bold")
text(838, 405, "TRUMP", 12, WHITE, "bold")

# Four key dispatches
card(28, 474, 474, 190, "Gulf • Escalation", "Drones strike Kuwait, Bahrain", "Iranian drones hit both Gulf states; the US strikes a missile site on Qeshm Island.", RED)
card(522, 474, 474, 190, "Ukraine • Black Sea", "Kerch Bridge partly collapses", "The bridge is damaged after Ukrainian drone and missile attacks.", BLUE)
card(28, 680, 474, 190, "United States • Senate", "Peltola wins Alaska seat", "Mary Peltola's victory gives Democrats a 56–44 Senate majority.", BLUE)
card(522, 680, 474, 190, "Technology • Nvidia", "Revenue doubles to $115.8bn", "Nvidia's board rejects former chief Jensen Huang's return as CEO.", GOLD)

# Health and weather closing band
d.rounded_rectangle((28, 886, 996, 994), radius=14, fill="#E6E2D8")
d.rectangle((28, 886, 36, 994), fill=RED)
text(54, 900, "HEALTH & WEATHER", 14, RED, "bold")
text(54, 924, "Measles-free status lost", 21, INK, "bold")
paragraph(54, 953, "US: 5,400+ cases, 10 deaths after 26 years. Ebola in DR Congo tops 11,000.", 14, 485, MUTED, 3, 2)
d.line((548, 902, 548, 978), fill="#C8C2B6", width=2)
text(570, 924, "Cyclone Akvan nears India's east coast", 19, INK, "bold")
paragraph(570, 954, "A powerful storm approaches the coast.", 14, 380, MUTED, 3, 2)

im.save("entry.png", format="PNG", optimize=True)
