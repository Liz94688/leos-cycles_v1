  /* Needed for the hamburger menu to work on a small screen */
  /* Also needs to be connected up to the settings.py and urls.py before it will work */

/* Easier way to do this?? */

  const hamburger = document.getElementById('hamburger');
    const navUL = document.getElementById('nav-ul');

    hamburger.addEventListener('click', () => {
        navUL.classList.toggle('show');
    });