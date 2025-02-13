// スクロールによるフェードイン効果
document.addEventListener('DOMContentLoaded', function() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, {
        threshold: 0.1  // 要素が10%見えた時点でアニメーション開始
    });

    // フェードインさせたい要素にクラスを追加して監視
    document.querySelectorAll('.scroll-fade').forEach((el) => observer.observe(el));
});

// スムーズスクロール
document.addEventListener('DOMContentLoaded', function() {
    // scroll クラスを持つリンクを探す
    document.querySelectorAll('a.scroll').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            // リンク先の要素を取得
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            // スムーズスクロール
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        });
    });
});