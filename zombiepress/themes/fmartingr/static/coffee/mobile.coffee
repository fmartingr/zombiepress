toggleMenu = ->
    sidebar = document.querySelector '.sidebar'
    button = document.querySelector 'button.menu'

    if 'menu-shown' in button.classList
        sidebar.classList.remove 'shown'
        button.classList.remove 'menu-shown'
    else
        sidebar.classList.add 'shown'
        button.classList.add 'menu-shown'

window.onload = ->
    button = document.querySelector 'button.menu'
    button.onclick = toggleMenu
