/**
 * @license Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
    config.toolbar = [
        { name: 'tools', items: [ 'Source', '-', 'Maximize' ]},
        { name: 'clipboard', items: [ 'Undo', 'Redo' ] },
        { name: 'styles', items: [ 'Bold', 'Italic', 'Underline', 'Strike' ] },
        { name: 'paragraph', groups: [ 'list', 'indent', 'blocks', 'align', 'bidi' ], items: [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'Code' ] },
        '/',
        { name: 'styles', items: [ 'Styles', 'Format', 'Link', 'Anchor' ] },
        { name: 'text', items: [ 'JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock' ]},
        { name: 'documents', items: ['Image', 'Table'] }
    ];
    config.toolbarCanCollapse = true;
};
