import webview

if __name__ == "__main__":
    # Point to your local index.html file
    webview.create_window("It Just Clicks Hub", "pages/index.html")
    webview.start()