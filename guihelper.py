def center_window(wnd, width=300, height=200):
    # get screen width and height
    screen_width = wnd.winfo_screenwidth()
    screen_height = wnd.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    wnd.geometry('%dx%d+%d+%d' % (width, height, x, y))