# Higher Order Functions

<table>
    <tr>
        <th>
            Plain JS
        </th>
        <th>
            Higher Order Function
        </th>
        <th>
            Arrow Function
        </th>
    </tr>
    <tr>
        <td>
            <code>
            for (let i = 0; i < companies.length; i++) {
                console.log(companies[i]);
}
            </code>
        </td>
        <td>
            <code>
            companies.forEach(function(company) {
                console.log(company.name);
            });
            </code>
        </td>
        <td>
            <code>
            companies.forEach(function(company) {
                console.log(company.name);
            });
            </code>
        </td>
    </tr>
    <tr>
        <td>
            <code>
            let canDrink = [];<br>
            for(let i = 0; i < ages.length; i++) {
                if(ages[i] >= 21) {
                    canDrink.push(ages[i]);
                }
            }
            </code>
        </td>
        <td>
            <code>
            const canDrink = ages.filter(function(age) {
                if(age >= 21) {
                    return true;
                }
            }
            </code>
        </td>
        <td>
            <code>
            const canDrink = ages.filter(age => age >= 21);
            </code>
        </td>
    </tr>
    <tr>
        <td>
            <code>
            for (let i = 0; i < companies.length; i++) {
                console.log(companies[i]);
}
            </code>
        </td>
        <td>
            <code>
            companies.forEach(function(company) {
                console.log(company.name);
            });
            </code>
        </td>
        <td>
            <code>
            companies.forEach(function(company) {
                console.log(company.name);
            });
            </code>
        </td>
    </tr>
</table>
