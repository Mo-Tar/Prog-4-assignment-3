"use strict";

module.exports.register = (app, database) => {

    app.get('/', async (req, res) => {
        res.status(200).send("This is running!").end();
    });

    //URL parameter to get Item with ID
    app.get('/api/items/:id', async (req, res) => {
        const _id = req.params.id;
        const query = database.query('SELECT * FROM Inventory WHERE ItemID = ?', [_id]);

        const inventoryItems = await query;

        res.status(200).send(JSON.stringify(inventoryItems)).end();
    });

    //Query parameter to get Item with name, if no query parameter, return all items.
    app.get('/api/items', async (req, res) => {
        let query;
        const _name = req.query.name;

        if (_name) {
            query = database.query('SELECT * FROM Inventory WHERE name =?',[_name]);
        } else {
            query = database.query('SELECT * FROM Inventory');
        }
        
        const inventoryItems = await query;

        if (inventoryItems.length === 0) {
            return res.status(404).json({ message: "No items found"});
        }

        res.status(200).send(JSON.stringify(inventoryItems)).end();
    });

    //Body parameter to add new items to inventory
    app.post('/api/items', async (req, res) => {
        const { ItemID, Name, Quantity, Price, SupplierID } = req.body;
        
        await database.query('INSERT INTO Inventory (ItemID, Name, Quantity, Price, SupplierID) values (?, ?, ?, ?, ?)', [ItemID, Name, Quantity, Price, SupplierID]);

        res.json({ status: "Success" });
    });

    //Modifying quantity of an item when given specific itemID
    app.put('/api/items', async (req, res) => {
        const { ItemID, Quantity } = req.body;
        
        await database.query('UPDATE Inventory SET Quantity = ? WHERE ItemID = ?', [Quantity, ItemID]);

        res.json({ status: "Success" });
    });

    //Delete an item if matching name or id
    app.delete('/api/items/:identifier', async (req, res) => {
        const identifier = req.params.identifier;
        let query = 'DELETE FROM INVENTORY WHERE ItemID = ?';
        let params = [identifier];

        if (isNaN(identifier)) {
            query = 'DELETE FROM INVENTORY WHERE Name = ?';
            params = [identifier];
        }

        const [results] = await database.query(query, params);

        if (results.affectedRows === 0) {
            res.json({ status: "Error", message: "No item with matching ID or name found" });
        } else {
            res.json({ status: "Success" });
        }
    });
};
