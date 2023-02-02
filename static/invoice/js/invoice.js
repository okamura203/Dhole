// 入力フォームでリターンキー押下時に送信させない
$('#myform').on('sumbit', function (e) {
    e.preventDefault();
});

// 連続送信防止
$('.save').on('click', function (e) {
    $('.save').addClass('disabled');
    $('#myform').submit();
});



//ブラウザバック禁止
history.pushState(null, null, location.href);
window.addEventListener('popstate', (e) => {
    history.go(1);
});

$(window).on("popstate", function (event) {
    history.pushState(null, null, null);
    window.alert('ブラウザバックできません。ブラウザを閉じてください');
});

