# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alex", color="#ff0000")
define m = Character("me", color="#0000ff")

# The game starts here.

label start:
        
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg coffee shop

    "You go to your favorite coffee shop and spot your friend Alex sitting at a small table, nervously sipping on a latte."
    "You go over to talk to them."
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alex sad at right

    # These display lines of dialogue.

    a "Hello..."
    m "Hey Alex! You look like you've seen a ghost. What's going on?"
    a "I've got a major career decision to make, and it's eating me alive."
    a "I've been offered a steady, well-paying job with great benefits, but it's in a city I've never been to. 
    I'd have to move away from everything I know."
    a "On the other hand, I've also received an offer to work for a startup in a field I'm passionate about, but it pays less, 
    and there's no guarantee of success."
    

    menu:
        "You decide to help Alex by telling them to..."

        "Choose security.":
            jump security

        "Pursue their passion":
            jump passion


label security:
        
    m " Stability can be important, Alex." 
    m "You've always wanted financial security. This job might provide that."

    show alex smile at right

    a "I guess you're right... I'll take the job. Thanks for helping me decide."
    
    hide alex
    scene bg street rainy

    "Alex chooses the secure job but feels unfulfilled." 
    "The new city is unfamiliar, and they struggle with loneliness and regret."

    m "Hi Alex! You seem distant how's the new job?"

    show alex gray sad

    a "It's secure, but it's not what I expected. I miss home, and I'm not happy."
    m " I'm so sorry Alex... "
    m "Hopefully things will turn out better in the future."
    "But Alex's regret and unhappiness continue..."

    "{b}Bad Ending{/b}."

    # This ends the game.
    return

label passion:
    m "Following your passion could lead to greater fulfillment." 
    m "It's a risk, but it might be worth it in the long run."

    show alex surprise at right

    a "I didn't think of it like that! I'll give it a try!"

    hide alex
    scene bg street sunny
    
    "Alex chooses to follow their passion."
    "Over time, they face challenges but find satisfaction in their work."
    "You support them throughout their journey."

    show alex happy
    
    m "Alex, I'm so glad you followed your passion."
    m "You're doing amazing work, and you're happier than ever."
    a " Thanks! I couldn't have done it without your support."
    "You both smile, knowing Alex made the right choice." 
    "You and Alex keep talking the afternoon away about all the fun things he's been doing."

    "{b}Good Ending{/b}."

    return

