categories = document.getElementsByClassName("menu-categories")[0];

if(isTouchDevice()){ //if touch events exist...

    categories.addEventListener("touchstart", function(event) {
        scrollStartPos=this.scrollLeft+event.touches[0].pageX;
    },false);

    categories.addEventListener("touchmove", function(event) {
        this.scrollLeft=scrollStartPos-event.touches[0].pageX;
    },false);
}

function isTouchDevice(){
try{
    document.createEvent("TouchEvent");
    return true;
}catch(e){
    return false;
}
}