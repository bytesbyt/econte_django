# Econte Lab

Econte Lab is a blog site that hopes to create a platform where like-minded individuals can keep motivated to live mindfully by sharing tips and strategies on how to become a mindful pereson.

It is available to the whole world aiming to enrich other people’s lives by providing content that can help hone a positive outlook toward life.

![Responsive Mockup](assets/docs/econte_mockup.png)

## Wireframes

Mobile first wireframes were created to show the basic layout of the website using Figma. This can be viewed on [Figma](https://www.figma.com/file/tn31GmaDQI9G27byM7oohP/Untitled?type=design&node-id=0%3A1&mode=design&t=Xah0acr87TvzVzTs-1)

- __Home Page__

  - Wireframe image below shows top and bottom mobile view of the Home page.

![Home Page]()

- __Blog Page__

  - Wireframe image below shows top and bottom mobile view of the Blog page.

![Blog Page]()

- __Subscibe Page__

  - Wireframe image below shows mobile view of the Subscribe page.

![Subscribe Page]()

## Features 

### Existing Features

- __Navigation Bar__

  - Featured at the top of the page, the navigation shows the blog name in the left corner: Econte.
  - Featured on all three pages on the right, the full responsive navigation bar includes links to the Home, Blog and Subscibe page and is identical in each page to allow for easy navigation.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button.
  - The navigation clearly tells the user the name website and makes the different sections of information easy to read.


 ![Navigation Bar]()

- __The landing page image__

  - The landing includes a photograph with text overlay to allow the user to see exactly which location this site would be applicable to. 
  - This section introduces the users of Econte with an eye catching zoom effect animation to grab their attention.

 ![Landing Page Image](assets/docs/econte_landing.png)

- __Video Section__

  - The video section will visually inspire and encourage the user to consider yoga as their form of practice for mindful living.

![Video Page](assets/docs/econte_video.png)

- __About Section__

  - About section will allow the users to understand what is mindfulness and see the benefits of joining the community of mindfulness. 
  - Users will see the value of signing up for the Econte blog subscription.

![About section]()

- __The Footer__ 

  - The footer section includes links to the relevant social media sites (Facebook, Youtube, Instagram) for Econte. The links will open to a new tab to allow easy navigation for the user. 
  - The footer is valuable to the user as it encourages them to keep connected via social media.

![Footer section](assets/docs/econte_footer.png)

- __Blog Page__

  - The blog page will provide the users with thoughtful contents to uplevel their life, focusing on mindfulness and personal growth.
  - This section is valuable to the user as the contents will be able to provide valuble insight and tips on living mindfully.

![Blog section]()

- __Subscribe Page__

  - This page will allow the user to subscibe for a dose of inspiration for mindful living. The user will be asked to submit their first name, last name and email address. 

![Subscribe page]()

### Features Left to Implement

- In the future, I would like to implement a feature where users can view and signup for mindfulness classes (provided by third party) arounds the world.
- Mindfulness classes such as meditation, soundbath and yoga etc. are the some of examples.

## Testing

 - Econte page works in differnet browsers: Chrome, Firefox, Safari 

 - This website is responsive, looks good and functions on all standard screen sizes using the devtool device toolbar.

 - Navigation menu will change to hamburger icon if viewed in smaller devices.

 - THa navigation, home, blog, and subscribe text are all readable and easy to understand.

 - Form in the subscribe page works: requires entries in every field, will only accept an email in the email field,  and the submit button works.

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
   - Index page:
![HTML Validator1](assets/docs/econte_html_index_validator.png)
   - About page:
![HTML Validator2](static/images/econte_html_about_validator.png)
   - Subscribe page:
![HTML Validator3](assets/docs/econte_html_subscribe_validator.png)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
![CSS Validator](assets/docs/econte_css_validator.png)
- Accessibility
  - Colors and fonts chosed are easy to read and accessible by running it throght lighthouse in devtools.
![Light House](assets/docs/econte_lighthouse.png)

### Solved Bugs
 
 - Split page function used for larger screens was not working.

 - This bug has been fixed by changing flex-direction in the media queries section to row from column.

   .split-screen {
    flex-direction: row;
    height: 100vh;
  }

 ### Unfixed Bugs

No unfixed bugs

## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://bytesbyt.github.io/econte/


## Credits

### Content 

- The text for the Home page and blog articles was taken from [Mellio Obrien](https://melliobrien.com/)
- The code to make the hero section was take from the [CI Love Running Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LRFX101+2023_Q2/courseware/e805068059af42af87681032aa64053f/1da6ad13213740f1855a51d30a2375b1/)
- The code to make the social media links was take from the [CI Love Running Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LRFX101+2023_Q2/courseware/e805068059af42af87681032aa64053f/1da6ad13213740f1855a51d30a2375b1/)
- The code to make the navigation was take from the [CI Love Running Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LRFX101+2023_Q2/courseware/e805068059af42af87681032aa64053f/1da6ad13213740f1855a51d30a2375b1/)
- The code to make subscibe page was take from the [CI Love Running Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LRFX101+2023_Q2/courseware/e805068059af42af87681032aa64053f/1da6ad13213740f1855a51d30a2375b1/)
- The hamburger icons in the navigation was taken from [Font Awesome](https://fontawesome.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- The responsive mock up image in ReadMe has been produced using [AmIResponsive?] (https://ui.dev/amiresponsive)


### Media

- The photos used on the home, blog and subscibe pages are from [Pexels](https://www.pexels.com/)
- The video used for the home page is from [Videvo](https://www.videvo.net/)