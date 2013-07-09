/**
 * @license Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
    config.extraPlugins = 'readmore';
    config.toolbar = [
        { name: 'tools', items: [ 'Source', '-', 'Maximize' ]},
        { name: 'clipboard', items: [ 'Undo', 'Redo' ] },
        { name: 'styles', items: [ 'Bold', 'Italic', 'Underline', 'Strike' ] },
        { name: 'paragraph', groups: [ 'list', 'indent', 'blocks', 'align', 'bidi' ], items: [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'Code' ] },
        '/',
        { name: 'styles', items: [ 'Styles', 'Format', 'Link', 'Anchor', 'ReadMore' ] },
        { name: 'text', items: [ 'JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock' ]},
        { name: 'documents', items: ['Image', 'Table'] }
    ];
    config.toolbarCanCollapse = true;

    CKEDITOR.on('instanceReady', function (ev) {
    // Ends self closing tags the HTML4 way, like <br>.
    ev.editor.dataProcessor.htmlFilter.addRules(
        {
            elements:
            {
                $: function (element) {
                    // Output dimensions of images as width and height
                    if (element.name == 'img') {
                        var style = element.attributes.style;

                        if (style) {
                            // Get the width from the style.
                            var match = /(?:^|\s)width\s*:\s*(\d+)px/i.exec(style),
                                width = match && match[1];

                            // Get the height from the style.
                            match = /(?:^|\s)height\s*:\s*(\d+)px/i.exec(style);
                            var height = match && match[1];

                            if (width) {
                                element.attributes.style = element.attributes.style.replace(/(?:^|\s)width\s*:\s*(\d+)px;?/i, '');
                                //element.attributes.width = width;
                            }

                            if (height) {
                                element.attributes.style = element.attributes.style.replace(/(?:^|\s)height\s*:\s*(\d+)px;?/i, '');
                                //element.attributes.height = height;
                            }
                        }
                    }



                    if (!element.attributes.style)
                        delete element.attributes.style;

                    return element;
                }
            }
        });
    });
};
