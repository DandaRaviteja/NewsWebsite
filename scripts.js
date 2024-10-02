const tabs = document.querySelectorAll('.tab');
const tabContents = document.querySelectorAll('.tab-content');
let leftVotes = 0;
let rightVotes = 0;

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        const target = tab.getAttribute('data-tab');
        tabContents.forEach(content => {
            content.classList.remove('active');
            if (content.id === target) {
                content.classList.add('active');
            }
        });
    });
});

function vote(side) {
    if (side === 'left') {
        leftVotes++;
    } else if (side === 'right') {
        rightVotes++;
    }
    updateVotes();
}

function updateVotes() {
    document.getElementById('left-votes').textContent = `Left Votes: ${leftVotes}`;
    document.getElementById('right-votes').textContent = `Right Votes: ${rightVotes}`;
    const totalVotes = leftVotes + rightVotes;
    const leftPercentage = (leftVotes / totalVotes) * 100;
    document.getElementById('bar').style.left = `${leftPercentage}%`;
}
