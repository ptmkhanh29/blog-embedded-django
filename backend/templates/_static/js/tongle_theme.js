document.addEventListener('DOMContentLoaded', function () {
    // Đặt tất cả code JavaScript liên quan đến DOM ở đây
    function toggleNightMode() {
        if (document.documentElement.getAttribute('data-theme') === 'light') {
            document.documentElement.setAttribute('data-theme', 'dark');
            document.getElementById('mode-switcher').classList.add('active');
            localStorage.setItem("theme", "dark");
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            document.getElementById('mode-switcher').classList.remove('active');
            localStorage.setItem("theme", "light");
        }
    }

    const modeSwitcher = document.getElementById('mode-switcher');
    if (modeSwitcher) {
        modeSwitcher.onclick = toggleNightMode;
    }

    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    if (currentTheme === 'dark') {
        modeSwitcher.classList.add('active');
    }
});
