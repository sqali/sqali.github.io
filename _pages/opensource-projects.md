---
title: "Open Source Projects"
permalink: /opensource-projects/
toc: true
toc_label: "Table of Contents"
toc_icon: "bookmark"
---

![SQAli's GitHub stats](https://github-readme-stats.vercel.app/api?username=sqali&show_icons=true)

## ![GitHub Avatar](https://avatars.githubusercontent.com/u/365630?s=48&v=4) Scikit Learn 

## ![GitHub Avatar](https://avatars.githubusercontent.com/u/34455048?s=48&v=4) Keras 

## 🤗 Huggingface

## ![GitHub Avatar](https://avatars.githubusercontent.com/u/5009934?s=48&v=4) OpenCV

## ![GitHub Avatar](https://avatars.githubusercontent.com/u/21003710?s=48&v=4) PyTorch

## ![GitHub Avatar](https://avatars.githubusercontent.com/u/1728152?s=40&v=4) Nvidia

## ![GitHub Avatar](https://avatars.githubusercontent.com/u/21206976?s=48&v=4) Pandas


## GitHub Contribution Graph

<!DOCTYPE html>
<html>
<head>
  <title>GitHub Contribution Graph</title>
  <!-- Include the Chart.js library -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
  <h1>GitHub Contribution Graph</h1>
  <canvas id="contribution-graph" width="800" height="400"></canvas>

  <script>
    // Make a GET request to the GitHub API to fetch the list of repositories
    fetch('https://api.github.com/users/{sqali}/repos')
      .then(response => response.json())
      .then(repositories => {
        // Array to store the contribution data for all repositories
        const allContributions = [];

        // Iterate over each repository and fetch its contribution data
        repositories.forEach(repository => {
          fetch(`https://api.github.com/repos/{sqali}/${repository.name}/stats/contributors`)
            .then(response => response.json())
            .then(data => {
              // Extract the contribution data from the response
              const contributions = data.map(contributor => contributor.total);

              // Add the contribution data to the array
              allContributions.push(...contributions);

              // Check if all repositories have been processed
              if (allContributions.length === repositories.length) {
                // Render the contribution graph on your page
                const ctx = document.getElementById('contribution-graph').getContext('2d');
                new Chart(ctx, {
                  type: 'line',
                  data: {
                    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    datasets: [{
                      label: 'Contributions',
                      data: allContributions,
                      backgroundColor: 'rgba(0, 123, 255, 0.5)',
                      borderColor: 'rgba(0, 123, 255, 1)',
                      borderWidth: 1
                    }]
                  },
                  options: {
                    responsive: true,
                    maintainAspectRatio: false
                  }
                });
              }
            })
            .catch(error => {
              console.error(`Error fetching contribution data for ${repository.name}:`, error);
            });
        });
      })
      .catch(error => {
        console.error('Error fetching repository data:', error);
      });
  </script>
</body>
</html>