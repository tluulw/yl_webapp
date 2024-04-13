categories = document.getElementsByClassName("menu-categories")[0];

categories.onmousedown = () => {
    let pageX = 0;
  
    document.onmousemove = e => {
      if (pageX !== 0) {
        categories.scrollLeft = categories.scrollLeft + (pageX - e.pageX);
      }
      pageX = e.pageX;
    };
  
    // заканчиваем выполнение событий
    categories.onmouseup = () => {
      document.onmousemove = null;
      categories.onmouseup = null;
    };
  
    // отменяем браузерный drag
    categories.ondragstart = () => {
      return false;
    };
  };