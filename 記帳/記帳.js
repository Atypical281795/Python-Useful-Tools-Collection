let activities = [];

function addActivity() {
    const activityName = document.getElementById('activity-name').value;
    if (activityName) {
        const newActivity = { name: activityName, items: [] };
        activities.push(newActivity);
        renderActivityList();
        document.getElementById('activity-name').value = '';
    } else {
        alert('請輸入活動名稱');
    }
}

function renderActivityList() {
    const activityList = document.getElementById('activity-list');
    activityList.innerHTML = '';
    activities.forEach((activity, index) => {
        const li = document.createElement('li');
        li.innerHTML = `<span>${activity.name}</span> <button onclick="viewActivity(${index})">查看</button>`;
        activityList.appendChild(li);
    });
}

function viewActivity(index) {
    const activity = activities[index];
    document.getElementById('activity-title').innerText = activity.name;
    document.getElementById('activity-details').style.display = 'block';
    document.getElementById('activities').style.display = 'none';
    renderItems(index);
}

function backToActivities() {
    document.getElementById('activity-details').style.display = 'none';
    document.getElementById('activities').style.display = 'block';
}

function addItem() {
    const activityTitle = document.getElementById('activity-title').innerText;
    const activityIndex = activities.findIndex(activity => activity.name === activityTitle);
    const itemName = document.getElementById('item-name').value;
    const itemAmount = document.getElementById('item-amount').value;
    const itemPerson = document.getElementById('item-person').value;
    const itemDate = document.getElementById('item-date').value;
    const itemAttachment = document.getElementById('item-attachment').files[0];

    if (itemName && itemAmount && itemPerson && itemDate) {
        const newItem = {
            name: itemName,
            amount: itemAmount,
            person: itemPerson,
            date: itemDate,
            attachment: itemAttachment ? itemAttachment.name : ''
        };
        activities[activityIndex].items.push(newItem);
        renderItems(activityIndex);
        clearItemInputs();
    } else {
        alert('請填寫所有項目');
    }
}

function renderItems(activityIndex) {
    const itemList = document.getElementById('item-list');
    itemList.innerHTML = '';
    activities[activityIndex].items.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `項目: ${item.name}, 金額: ${item.amount}, 請款人: ${item.person}, 日期: ${item.date}, 附件: ${item.attachment}`;
        itemList.appendChild(li);
    });
}

function clearItemInputs() {
    document.getElementById('item-name').value = '';
    document.getElementById('item-amount').value = '';
    document.getElementById('item-person').value = '';
    document.getElementById('item-date').value = '';
    document.getElementById('item-attachment').value = '';
}

document.addEventListener('DOMContentLoaded', () => {
    renderActivityList();
});
