window.onload = ->
    if document.querySelector '[name="content"]'
        CKEDITOR.replace 'content',
            customConfig: '/static/ckeditor/config.js'
