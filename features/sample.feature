Feature: showing off behave

  Scenario: run a simple test
     Given User click on "./images/search.png"
     When User type "notepad"
     Given User click on "./images/notepad.png"
     When User maximize window
     When User type "Hello World"
     Given User click on "./images/note_pad_images/file_menu.png"
     Then User should see 
     """
     ["./images/note_pad_images/file_items/new_tab_item.png",
     "./images/note_pad_images/file_items/new_tab_hotkey.png",
     "./images/note_pad_images/file_items/new_window_item.png",
     "./images/note_pad_images/file_items/new_window_hotkey.png",
     "./images/note_pad_images/file_items/open_item.png",
     "./images/note_pad_images/file_items/open_hotkey.png",
     "./images/note_pad_images/file_items/save_item.png",
     "./images/note_pad_images/file_items/save_hotkey.png"]
     """
     When User press hot key "['ctrl', 's']"
     When User perform save action with path "D:\ChongYeu\pyautogui_sample\outputs" and file name "vuongledai"
     Given User click on "./images/close.png"
     When User open "D:\ChongYeu\pyautogui_sample\outputs"
     Given User double click on "./images/expected_images/vuongledai.png"
     Then User should see 
     """
     ["./images/expected_images/hello_world.png"]
     """
#Clear Data after Test
     Given User click on "./images/close.png"
     Given User click on "./images/close.png"
     When Delete file "D:\ChongYeu\pyautogui_sample\outputs\vuongledai.txt"
    

