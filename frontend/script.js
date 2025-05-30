document.addEventListener('DOMContentLoaded', function() {
    const matchesList = document.getElementById('matches-list');
    const loadingElement = document.getElementById('loading');
    const errorElement = document.getElementById('error');
    
    // Fetch matches from our backend
    fetch('http://localhost:5000/api/matches')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            loadingElement.classList.add('hidden');
            
            if (data.error) {
                errorElement.textContent = `Error: ${data.error}`;
                return;
            }
            
            if (data.matches && data.matches.length > 0) {
                data.matches.forEach(match => {
                    const matchElement = document.createElement('div');
                    matchElement.className = 'match-card';
                    
                    matchElement.innerHTML = `
                        <div class="teams">${match.homeTeam} vs ${match.awayTeam}</div>
                        <div class="date">${match.date}</div>
                    `;
                    
                    matchesList.appendChild(matchElement);
                });
            } else {
                matchesList.innerHTML = '<p>No upcoming matches found.</p>';
            }
        })
        .catch(error => {
            loadingElement.classList.add('hidden');
            errorElement.textContent = `Failed to load matches: ${error.message}`;
            console.error('Error:', error);
        });
});