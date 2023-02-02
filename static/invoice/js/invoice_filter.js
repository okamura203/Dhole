function doReload() {

    // reloadメソッドによりページをリロード
    window.location.reload();
}

window.addEventListener('load', function () {

    // ページ表示完了した15秒後にリロード
    setTimeout(doReload, 15000);
});

// [検索を解除] の表示制御
conditions = $('#filter').serializeArray();
$.each(conditions, function () {
    if (this.value) {
        $('.filtered').css('visibility', 'visible')
    }
});