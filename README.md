 ## Flask Application Design for Open Office Booking System

### HTML Files

**1. `index.html`**
- This is the landing page of the application.
- It displays a welcome message and provides a link to the registration page.

**2. `register.html`**
- This page allows users to register their open office 1-hour slots.
- It includes a form with fields for the user's name, email, and the date and time of their available slots.

**3. `book.html`**
- This page allows users to book available office slots.
- It displays a list of registered slots and allows users to select and book a slot.

**4. `confirmation.html`**
- This page is displayed after a user successfully books a slot.
- It displays a confirmation message and provides a link to the user's profile.

**5. `profile.html`**
- This page displays the user's profile, including their registered slots and booked slots.
- It also allows users to edit their profile information.

### Routes

**1. `/`**
- This route handles the landing page of the application.
- It renders the `index.html` file.

**2. `/register`**
- This route handles the registration of open office slots.
- It processes the form data from the `register.html` file and saves the slot information to the database.
- It then redirects the user to the `confirmation.html` page.

**3. `/book`**
- This route handles the booking of available office slots.
- It retrieves the list of registered slots from the database and displays them on the `book.html` page.
- It processes the form data from the `book.html` file and updates the database to mark the selected slot as booked.
- It then redirects the user to the `confirmation.html` page.

**4. `/profile`**
- This route handles the display of the user's profile.
- It retrieves the user's information and registered slots from the database and displays them on the `profile.html` page.
- It also processes the form data from the `profile.html` file and updates the user's information in the database.

**5. `/edit`**
- This route handles the editing of the user's profile.
- It retrieves the user's information from the database and displays it on the `edit.html` page.
- It processes the form data from the `edit.html` file and updates the user's information in the database.
- It then redirects the user to the `profile.html` page.