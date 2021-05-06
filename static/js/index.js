
// Upload PDF

$('#btn-upload-pdf').on('click', function () {
    $('#upload-pdf').trigger("click");
});
$('#upload-pdf').change(function () {
    let file = $('#upload-pdf').prop('files')[0];
    if (!file) {
        return;
    }
    let file_name = this.value.replace(/\\/g, '/').replace(/.*\//, '');
    $('#fileNameUpload').text(file_name);
});

// Upload Image

$('#btn-upload-front-pdf').on('click', function () {
    $('#upload-front-pdf').trigger("click");
});
$('#upload-front-pdf').change(function () {
    let file = $('#upload-front-pdf').prop('files')[0];
    if (!file) {
        return;
    }
    let reader = new FileReader();
    let file_name = this.value.replace(/\\/g, '/').replace(/.*\//, '');
    reader.onload = function (e) {
        $('#front-pdf')
            .attr('src', e.target.result)
            .width(150)
            .height(200);
    };
    reader.readAsDataURL(file);
    $('#frontUpload').text(file_name);
});