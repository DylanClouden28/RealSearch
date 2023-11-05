// gamble.js
document.addEventListener('DOMContentLoaded', (event) => {
    const options = [
      "I am trying to build a webserver what backend should I use",
      "What is the best theme park to go to in the US",
      "What is a hackathon, how can I prepare",
      "Can you give some advice I am going to college",
      "What kind of car do you recommend",
      "What are the best places to go in Buffalo"
    ];
  
    const gambleButton = document.querySelector('.bg-green-500'); // adjust the selector if needed
    const searchInput = document.querySelector('input[name="search"]');
  
    gambleButton.addEventListener('click', function() {
      const randomOption = options[Math.floor(Math.random() * options.length)];
      searchInput.value = randomOption;
      document.getElementById('searchButton').click();
    });
  });
  