# Import the Playwright tool so we can control the browser
from playwright.sync_api import sync_playwright

# Start the Playwright session
with sync_playwright() as playwright:
    
    # Launch a Chromium browser. headless=False means we get to watch it happen on screen
    browser = playwright.chromium.launch(headless=True)
    
    # Open a new blank page (tab) in the browser
    page = browser.new_page()

    print("Director: Going to Wikipedia...")
    # Tell the browser to navigate to the Wikipedia homepage
    page.goto("https://en.wikipedia.org/")

    print("Director: Typing 'Automation tools' into the search box...")
    # Find the search input box by its ID (#searchInput) and type our word
    # (We added "tools" so it doesn't redirect automatically)
    page.fill("#searchInput", "Automation tools")

    print("Director: Pressing Enter to search...")
    # PRO TIP: Instead of clicking a button (which breaks when websites update), 
    # we just simulate pressing the Enter key on the keyboard!
    page.keyboard.press("Enter")

    print("Director: Waiting for the results page to load...")
    # Tell the script to pause and wait until the search results container appears on screen
    page.wait_for_selector(".mw-search-results")

    print("Director: Extracting the first 3 titles...")
    # Find all the title links inside the search results area
    all_title_elements = page.locator(".mw-search-results .mw-search-result-heading a").all()
    
    # Grab only the first 3 items from the list we just found
    top_3_titles = all_title_elements[:3]

    # Open a new text file in "write" mode to save our data
    with open("wiki_output.txt", "w") as file:
        
        # Loop through our 3 titles one by one
        for title_element in top_3_titles:
            # Extract the actual text (words) from the HTML element
            text = title_element.text_content()
            print(f"Found title: {text}")
            
            # Write the text to our file, and add a newline (\n) so they stack nicely
            file.write(text + "\n")

    print("Director: Mission accomplished. Closing browser.")
    # Close the browser to free up computer memory
    browser.close()