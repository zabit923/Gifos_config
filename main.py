import gifos, colorama
from colorama import Fore

colorama.init()

t = gifos.Terminal(font_file='CascadiaCodePL.ttf', width=800, height=600, xpad=5, ypad=5, font_size=15)

t.set_fps(15)


def reg_line(text, row, delay=2, color="white", contin=False, save=True):
    t.set_txt_color(color)
    t.gen_text(text=text, row_num=row, contin=contin)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")


def shell(row, delay=0, color="white", contin=False, save=True):
    t.set_txt_color(color)
    t.gen_text(text="[zabit923@zabit-desktop ~]$ ", row_num=row, contin=contin)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")


def typetext(text, row, delay=1, color="white", contin=True, save=True):
    t.clone_frame(3)
    for char in text:
        t.set_txt_color(color)
        t.gen_text(text=char, row_num=row, contin=contin)
        t.clone_frame(delay)
        if save:
            t.save_frame(base_file_name=f"frame_{row}")
        t.set_txt_color("white")


def blankspace(row, delay=0, color="white", contin=False, save=True):
    t.set_txt_color(color)
    t.gen_text(text="     ", row_num=row, contin=contin)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")


def sys_line(text, row, delay=2, color="white", contin=False, save=True):
    t.gen_text(text=Fore.GREEN + "* " + Fore.WHITE + text, row_num=row, contin=contin)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")


def sys_line_ok(text, row, max_width=72, delay=2, color="white", contin=False, save=True):
    padding = max_width - len(text) - 1  # Subtract  1 for the space before "OK"
    if padding < 0:
        padding = 0
    padded_text = text + " " * padding

    t.gen_text(text=Fore.GREEN + "* " + Fore.WHITE + padded_text, row_num=row, contin=contin)
    t.clone_frame(delay)
    t.gen_text("[ " + Fore.GREEN + "ok" + Fore.WHITE + " ]", row_num=row, contin=True)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")


reg_line("Loading Linux 22.04.3 LTS x86_64 ...", 1, delay=0)
reg_line("Loading initial ramdisk ...", 2, delay=5)
t.clone_frame(30)

t.clear_frame()
reg_line("Freeing unused kernel memory: 980K (ffffffff81bcf000 - ffffffff81cc4000)", 1, delay=0)
reg_line("INIT: version 3.00 booting", 2, delay=0)
blankspace(3)
blankspace(5)
sys_line_ok("Mounting /proc ...", 6, delay=2)
sys_line_ok("Mounting /run ...", 7, delay=2)
sys_line("/run/lock: creating directory", 9, delay=0)
sys_line("/run/lock: correcting owner", 10, delay=0)
sys_line_ok("Caching service dependencies ...", 11, delay=0)
sys_line_ok("Mounting devtmpfs on /dev ...", 12, delay=0)
sys_line_ok("Mounting /dev/mqueue ...", 13, delay=7)
sys_line_ok("Mounting /dev/pts ...", 14, delay=0)
sys_line_ok("Mounting /dev/shm ...", 15, delay=0)
sys_line_ok("Creating list of required static device nodes for the current kernel . ", 16, delay=0)
sys_line_ok("Mounting /sys ...", 17, delay=0)
sys_line_ok("Mounting debug filesystem ...", 18, delay=4)
sys_line_ok("Mounting config filesystem ...", 19, delay=2)
sys_line_ok("Mounting cgroup filesystem ...", 20, delay=1)
sys_line_ok("Mounting fuse control filesystem ...", 21, delay=0)
sys_line_ok("Setting up tmpfiles.d entries for /dev ...", 22, delay=0)
sys_line_ok("Starting udev ...", 23, delay=0)
sys_line_ok("Generating a rule to create a /dev/root symlink ...", 24, delay=0)
sys_line_ok("Populating /dev with existing devices through uevents ...", 25, delay=0)
sys_line_ok("Waiting for uevents to be processed ...", 26, delay=0)
sys_line_ok("Setting system clock using the hardware clock [Local Time] ...", 27, delay=3)
sys_line("Configuring kernel parameters ...", 28, delay=0)
sys_line("Activating swap devices ...", 29, delay=0)
sys_line_ok("Setting hostname to gentoo ...", 30, delay=0)
sys_line("Autoloaded 18 module(s)", 31, delay=2)
sys_line_ok("Checking local filesystems ...", 32, delay=5)
reg_line("ubuntu_x86: clean, 786432/786432 files... ", 33, delay=0)
sys_line_ok("Remounting root filesystem read/write ...", 34, delay=0)
sys_line_ok("Remounting filesystems ...", 35, delay=2)
sys_line("Skipping mtab update (mtab is a symbolic link)", 36, delay=0)
sys_line_ok("Mounting local filesystems ...", 37, delay=2)
sys_line("setting up tmpfiles.d entries ...", 38, delay=0)
sys_line("Initializing random number generator ...", 39, delay=0)
sys_line("Activating additional swap space ...", 40, delay=0)
sys_line_ok("Mounting misc binary format filesystem ...", 41, delay=0)
reg_line("tmpfiles: ignoring invalid entry on line 15 of `/usr/lib/tmpfiles.d//tmp.conf`", 42, delay=0)
reg_line("tmpfiles: ignoring invalid entry on line 16 of `/usr/lib/tmpfiles.d//tmp.conf`", 43, delay=0)
sys_line("Creating user login records ...", 44, delay=0)
sys_line_ok("Loading custom binary format handlers ...", 45, delay=0)
sys_line_ok("Clearing /var/run ...", 46, delay=0)
sys_line_ok("Wiping /tmp directory ...", 47, delay=0)
sys_line("Setting terminal encoding [UTF-8] ...", 48, delay=0)
sys_line_ok("Bringing up interface lo", 49, delay=0)
sys_line_ok("Setting keyboard mode [UTF-8] ...", 50, delay=0)
sys_line_ok("Loading key mappings [en_US] ...", 51, delay=0)
sys_line_ok("   127.0.0.1/8 ...", 52, delay=0)
sys_line("   Adding routes", 53, delay=0)
sys_line_ok("      127.0.0.0/8 via 127.0.0.1 ...", 54, delay=0)
reg_line("INIT: Entering runlevel: 3", 55, delay=0)
sys_line_ok("Starting D-BUS system messagebus ...", 56, delay=0)
sys_line_ok("Starting syslog-ng ...", 57, delay=0)
sys_line("Starting DHCP Client Daemon ...", 58, delay=0)
sys_line("Starting ConsoleKit daemon ...", 59, delay=0)
sys_line_ok("Starting vixie-cron ...", 60, delay=0)
sys_line_ok("Starting local ...", 61, delay=0)
blankspace(62)
blankspace(63)
blankspace(64)
reg_line("Ubuntu Linux 22.04.3 LTS", 65, delay=0)
blankspace(66)
reg_line("ubuntu login: ", 66, delay=0)
typetext("zabit923", 66)
reg_line("password: ", 67, delay=0)
typetext("**********", 67)
blankspace(68)
blankspace(69)
shell(70)
typetext("pfetch", 70, contin=True)
blankspace(71)


reg_line(Fore.RED + "            .-/+oossssoo+/-.               " + Fore.RED + "zabit923" + Fore.WHITE + "@" + Fore.RED + "zabit-desktop", 72,delay=0)
reg_line(Fore.RED + "        `:+ssssssssssssssssss+:`           " + Fore.RED + 'OS: ' + Fore.WHITE + "Ubuntu 22.04.3 LTS x86_64", 73, delay=0)
reg_line(Fore.RED + "      -+ssssssssssssssssssyyssss+-         " + Fore.RED + 'Kernel: ' + Fore.WHITE + " 6.5.0-18-generic", 74, delay=0)
reg_line(Fore.RED + "    .ossssssssssssssssss" + Fore.WHITE + 'dMMMNy' + Fore.RED + "sssso.       " + Fore.RED + "Packages: " + Fore.WHITE + "2241", 75, delay=0)
reg_line(Fore.RED + "   /sssssssssss" + Fore.WHITE + 'hdmmNNmmyNMMMMh' + Fore.RED + "ssssss/      " + Fore.RED + "Shell: " + Fore.WHITE + "zsh 5.8.1", 76, delay=0)
reg_line(Fore.RED + "  +sssssssss" + Fore.WHITE + 'hm' + Fore.RED + "yd" + Fore.WHITE +'MMMMMMMNddddy' + Fore.RED + "ssssssss+     " + Fore.RED + "Resolution: " + Fore.WHITE + "1920x1080", 77, delay=0)
reg_line(Fore.RED + " /ssssssss" + Fore.WHITE + 'hNMMM' + Fore.RED + "yh" + Fore.WHITE + 'hyyyyhmNMMMNh' + Fore.RED + "ssssssss/    " + Fore.RED + "DE: " + Fore.WHITE + "GNOME 42.9", 78, delay=0)
reg_line(Fore.RED + ".ssssssss" + Fore.WHITE + 'dMMMNh' + Fore.RED + "ssssssssss" + Fore.WHITE + 'hNMMMd' + Fore.RED + "ssssssss.   " + Fore.RED + "WM: " + Fore.WHITE + "Mutter", 79, delay=0)
reg_line(Fore.RED + "+ssss" + Fore.WHITE + 'hhhyNMMNy' + Fore.RED + "ssssssssssss" + Fore.WHITE + 'yNMMMy' + Fore.RED + "sssssss+   " + Fore.RED + "WM Theme: " + Fore.WHITE + "Adwaita", 80, delay=0)
reg_line(Fore.RED + "oss" + Fore.WHITE + 'yNMMMNyMMh' + Fore.RED + "ssssssssssssss" + Fore.WHITE + 'hmmmh' + Fore.RED + "ssssssso   " + Fore.RED + "Theme: " + Fore.WHITE + "Yaru-magenta-dark [GTK2/3]", 81, delay=0)
reg_line(Fore.RED + "oss" + Fore.WHITE + 'yNMMMNyMMh' + Fore.RED + "sssssssssssssshmmmhssssssso   " + Fore.RED + "Icons: " + Fore.WHITE + "Yaru-magenta [GTK2/3]", 82, delay=0)
reg_line(Fore.RED + "+ssss" + Fore.WHITE + 'hhhyNMMNy' + Fore.RED + "ssssssssssss" + Fore.WHITE + 'yNMMMy' + Fore.RED + "sssssss+   " + Fore.RED + "Terminal: " + Fore.WHITE + "gnome-terminal", 83, delay=0)
reg_line(Fore.RED + ".ssssssss" + Fore.WHITE + 'dMMMNh' + Fore.RED + "ssssssssss" + Fore.WHITE + 'hNMMMd' + Fore.RED + "ssssssss.   " + Fore.RED + "CPU: " + Fore.WHITE + "AMD Ryzen 5 2600 [37.2°C]", 84, delay=0)
reg_line(Fore.RED + " /ssssssss" + Fore.WHITE + 'hNMMM' + Fore.RED + "yh" + Fore.WHITE + 'hyyyyhdNMMMNh' + Fore.RED + "ssssssss/    " + Fore.RED + "GPU: " + Fore.WHITE + "NVIDIA GeForce GTX 1650", 85, delay=0)
reg_line(Fore.RED + "  +sssssssss" + Fore.WHITE + 'dm' + Fore.RED + "yd" + Fore.WHITE + 'MMMMMMMMddddy' + Fore.RED + "ssssssss+     " + Fore.RED + "Memory: " + Fore.WHITE + "4570MiB / 15907MiB", 86, delay=0)
reg_line(Fore.RED + "   /sssssssssss" + Fore.WHITE + 'hdmNNNNmyNMMMMh' + Fore.RED + "ssssss/      ", 87, delay=0)
reg_line(Fore.RED + "    .ossssssssssssssssss" + Fore.WHITE + 'dMMMNy' + Fore.RED + "sssso.       ", 88, delay=0)
reg_line(Fore.RED + "      -+sssssssssssssssss" + Fore.WHITE + 'yyy' + Fore.RED + "ssss+-         ", 89, delay=0)
reg_line(Fore.RED + "        `:+ssssssssssssssssss+:`           ", 90, delay=0)
reg_line(Fore.RED + "            .-/+oossssoo+/-.               ", 91, delay=0)
blankspace(92)
shell(93)
t.clone_frame(94)

typetext("ghfetch -u zabit923", 95)

gh_stats = gifos.utils.fetch_github_stats("zabit923")
details_lines = f"""\\x1b[0m\x1b[96mTotal Commits: \x1b[93m{gh_stats.total_commits_all_time}\x1b[0m
\x1b[96mTotal PRs: \x1b[93m{gh_stats.total_pull_requests_made}\x1b[0m
\x1b[96mMerged PR %: \x1b[93m{gh_stats.pull_requests_merge_percentage}\x1b[0m
\x1b[96mTotal Contributions: \x1b[93m{gh_stats.total_repo_contributions}\x1b[0m
"""
blankspace(96)
reg_line(text=details_lines, row=97, delay=0)

blankspace(98)
shell(99)

typetext("cat /proc/languages | head -n 6", 100)

blankspace(101)

t.gen_text(text="\x1b[34mPython", row_num=102)
t.gen_text(text="\x1b[33mJavaScript", row_num=103)
t.gen_text(text="\x1b[31mHTML", row_num=104)
t.gen_text(text="\x1b[36mCSS", row_num=105)

blankspace(106)

typetext("cat /proc/frameworks | head -n 2", 106)

t.gen_text(text="\x1b[32mDjango", row_num=107)
t.gen_text(text="\x1b[31mDjango rest-framework", row_num=108)
t.gen_text(text="\x1b[37mFlask", row_num=109)

blankspace(110)

shell(111)
t.clone_frame(112)
typetext("poweroff", 113)
sys_line("Stopping local ...", 114, delay=0)
sys_line("Saving random seed ...", 115, delay=0)
sys_line("Unmounting network filesystems ...", 118, delay=0)
sys_line("Stopping cronie ...", 116, delay=0)
sys_line("Stopping NetworkManager ...", 117, delay=0)
sys_line("Stopping elogind ...", 118, delay=0)
sys_line("Stopping dbus ...", 119, delay=0)
sys_line("Unmounting loop devices ...", 120, delay=0)
sys_line("Unmounting filesystems ...", 121, delay=0)
sys_line("   Unmounting /efi ...", 122, delay=0)
sys_line("Deactivating swap devices ...", 123, delay=0)
sys_line("Setting hardware clock using the system clock [Local Time]...", 120, delay=0)
sys_line("Stopping udev ...", 124, delay=0)
sys_line("Terminating remaining processes ...", 125, delay=2)
sys_line("Killing remaining processes ...", 126, delay=0)
sys_line("Saving dependency cache ...", 127, delay=0)
sys_line("Remounting remaining filesystems read-only ...", 128, delay=0)
sys_line("   Remounting / read only ...", 129, delay=0)
reg_line("Sending the final term signal", 130, delay=30)
reg_line("Sending the final term signal", 131, delay=0)

blankspace(132)

t.clear_frame()
t.clone_frame(60)

t.gen_gif()
