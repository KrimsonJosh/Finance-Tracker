// Fetch expenses from /app/routes/dashboard_routes restapi
function fetchExpenses(){
    fetch('/api/expenses')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('expenseList'); // Lives in dashboard.html
            list.innerHTML = ''; 
            data.expenses.forEach(expense =>{
                const item = document.createElement('li');
                item.className = 'list-group-item';
                item.textContent = `Amount: $${expense.amount}, Category: ${expense.category}`; // Expense.amount, Expense.category from models.py
                list.appendChild(item)
            })
        })
        .catch(err => console.error('Error fetching amount/category:', err));
}
// Handle form submission to add expense;
document.getElementById('expenseForm').addEventListener('submit', function(e){
    const formData = new FormData(this);

    fetch('/api/expenses',{
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data =>{
        alert(data.message);
        fetchExpenses();
    })
    .catch(err => console.error('Error adding expense', err));
})

fetchExpenses();