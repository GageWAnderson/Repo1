function openSlideMenu(){
    console.log("Opening Sidebar");
    document.getElementById('side-menu').style.width = '250px';
    document.getElementById('main').style.marginLeft = '250px';
}

function closeSlideMenu(){
    console.log("Closing sidebar");
    document.getElementById('side-menu').style.width = '0px';
    document.getElementById('main').style.marginLeft = '0px';
}

function toggleSlideMenu(){
    if(document.getElementById('side-menu').style.width == '250px'){
        closeSlideMenu();
    }
    else{
        openSlideMenu();
    }
}