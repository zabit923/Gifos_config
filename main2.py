import gifos


t = gifos.Terminal(
    font_file='CascadiaCodePL.ttf',
    width=800,
    height=600,
    xpad=5,
    ypad=5,
    font_size=16,
)

t.set_fps(15)


def boot_line(text, row, delay=2, color="white", contin=False, save=True):
    t.set_txt_color(color)
    t.gen_text(text=text, row_num=row, contin=contin)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")


def init_line(text, row, save=True):
    t.gen_text("[ ", row_num=row)
    t.set_txt_color("green")
    t.gen_text("OK", row_num=row, contin=True)
    t.set_txt_color("white")
    t.gen_text(" ] ", row_num=row, contin=True)
    t.gen_text(text=text, row_num=row, contin=True)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")


def print_dots_done(row, delay=2):
    boot_line(".", row, delay, contin=True)
    boot_line(".", row, delay, contin=True)
    boot_line(".", row, delay, contin=True)
    boot_line(" Done", row, delay, contin=True, color="green")


boot_line("zabit ltd bios.js initializing", 1, delay=5)
print_dots_done(1)
boot_line("Hardware detection", 3, delay=2)
print_dots_done(3)

boot_line("Hardware detected:", 4)
boot_line("  CPU: AMD Ryzen 5 2600", 5, delay=2)
boot_line("  RAM: 15907MiB", 6, delay=2)
boot_line("  Display: 800x600 16-bit color GitHub Markdown Renderer", 7, delay=2)
t.clone_frame(15)

boot_line("Beginning memory test...", 9, delay=4)

# Memory test simulation
for i in range(0, 262144, 8192):  # 256MiB Memory
    t.delete_row(9)
    t.gen_text(f"Beginning memory test... {i}KiB", 9)

t.delete_row(9)
boot_line(f"Beginning memory test...", 9)
boot_line(" 262144KiB OK", 9, color="green", contin=True)
t.clone_frame(15)

t.clear_frame()

# Simulate the kernel boot process
boot_line("zabit ltd kernel.js initializing", 1)
print_dots_done(1)
init_line("Starting system...", 2)
init_line("Initializing hardware...", 3)
init_line("Checking filesystems...", 4)
init_line("Mounting volumes...", 5)
init_line("Starting networking service...", 6)
init_line("Initializing display...", 7)
t.gen_text("Welcome to zabit's profile!", 9)
t.clone_frame(15)
t.clear_frame()

# Simulate login prompt
t.set_font("CascadiaCodePL.ttf", 15)
t.gen_text(text="github login: ", row_num=1)
t.gen_typing_text(text="zabit923", row_num=1, col_num=14, contin=True, speed=0.1)
t.clone_frame(10)
t.gen_text(text="Password: ", row_num=2)
t.gen_typing_text(text="**********", row_num=2, col_num=10, contin=True, speed=0.1)
t.clone_frame(15)

t.clear_frame()
t.gen_text(text="Welcome, zabit923! Last Login: 01-01-1970T00:00:01", row_num=1)
t.set_prompt("\x1b[35mzabit923\x1b[39m@\x1b[32mgithub\x1b[39m:~$ ")
t.gen_prompt(2)
t.gen_typing_text(text="ghfetch -u zabit923", row_num=2, contin=True, speed=0.1)

gh_stats = gifos.utils.fetch_github_stats("zabit923")
details_lines = f"""\x1b[96mTotal Stars Earned: \x1b[93m{gh_stats.total_stargazers}\x1b[0m
\x1b[96mTotal Commits: \x1b[93m{gh_stats.total_commits_all_time}\x1b[0m
\x1b[96mTotal PRs: \x1b[93m{gh_stats.total_pull_requests_made}\x1b[0m
\x1b[96mMerged PR %: \x1b[93m{gh_stats.pull_requests_merge_percentage}\x1b[0m
\x1b[96mTotal Contributions: \x1b[93m{gh_stats.total_repo_contributions}\x1b[0m
"""
t.gen_text(text=details_lines, row_num=3)

t.gen_prompt(9)
t.gen_typing_text(
    text="cat /proc/languages | head -n 4", row_num=9, contin=True, speed=0.1
)

t.gen_text(text="\x1b[34mPython", row_num=11)
t.gen_text(text="\x1b[33mJavaScript", row_num=12)
t.gen_text(text="\x1b[31mHTML", row_num=13)
t.gen_text(text="\x1b[36mCSS", row_num=14)


t.gen_prompt(14)
t.gen_typing_text(
    text="cat /proc/frameworks | head -n 2", row_num=15, contin=True, speed=0.1
)
t.gen_text(text="\x1b[32mDjango", row_num=16)
t.gen_text(text="\x1b[31mDjango rest-framework", row_num=17)
t.gen_text(text="\x1b[37mFlask", row_num=18)


t.gen_prompt(26)
t.clone_frame(60)
t.gen_typing_text("reboot", 26, contin=True, speed=0.1)
t.clone_frame(5)
t.clear_frame()
init_line("Stopping system...", 1)
t.clone_frame(10)
t.clear_frame()
boot_line("System halted.", 1)
t.clone_frame(10)


t.gen_gif()
