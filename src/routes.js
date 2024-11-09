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
        if(inventoryItems.length === 0){
            return res.status(404).json({ error: "Cannot find Item ID" });
        }
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

    //Gets the name of suppliers and show all suppliers
    app.get('/api/suppliers', async (req, res) => {
        let query;
        const _name = req.query.name;

        if (_name) {
            query = database.query('SELECT * FROM Suppliers WHERE Name =?',[_name]);
        } else {
            query = database.query('SELECT * FROM Suppliers');
        }
        
        const supplier = await query;

        if (supplier.length === 0) {
            return res.status(404).json({ message: "No items found"});
        }

        res.status(200).send(JSON.stringify(supplier)).end();
    });

    app.post('/api/items', async (req, res) => {
        try {
 
            const { ItemID, Name, Quantity, Price, SupplierID } = req.body;
            
            if (!ItemID || !Name || Quantity === undefined || Price === undefined || !SupplierID) {
                return res.status(400).json({ error: "All fields ItemID, Name, Quantity, Price, SupplierID are required." });
            }
    
    
            const result = await database.query(
                'INSERT INTO Inventory (ItemID, Name, Quantity, Price, SupplierID) VALUES (?, ?, ?, ?, ?)',
                [ItemID, Name, Quantity, Price, SupplierID]
            );
    
           
            if (result.affectedRows === 0) {
                return res.status(500).json({ error: "Failed to insert item into inventory." });
            }


    
            res.json({ status: "Success", insertedItemID: result.insertId });
        } catch (error) {
            console.error("Error inserting item:", error);

            if (error.code === 'ER_DUP_ENTRY') {
                res.status(409).json({ error: "An item with the same ItemID already exists." });
            } else {
                res.status(500).json({ error: "An error occurred while adding the item." });
            }
        }
    });
    

    //Modifying quantity of an item when given specific itemID
    app.put('/api/items', async (req, res) => {
        try {

        const { ItemID, Quantity } = req.body;

        const inventoryItems = await database.query('UPDATE Inventory SET Quantity = ? WHERE ItemID = ?', [Quantity, ItemID]);

        if (!ItemID && !Quantity) {
            return res.status(400).json({ error: "Please provide 'ItemID' and 'Quantity' in the body" });
        }

        if (inventoryItems.affectedRows === 0){
            return res.status(400).json({ error: "No items found" });
        }
        else {
            res.json({ status: "Success" });
        }

        } catch {
            console.error("Error updating item:", error);
            res.status(500).json({ error: "An error occurred while updating the item." });
        }
    });

    //Deletes an item when given name or id
    app.delete('/api/items/', async (req, res) => {
        try {
            let query;
            const _name = req.query.name;
            const _id = req.query.id;
            

            if (!_name && !_id) {
                return res.status(400).json({ error: "Please provide either 'name' or 'id' as a query parameter." });
            }
    

            if (_name) {
                query = database.query('DELETE FROM Inventory WHERE name = ?', [_name]);
            } else if (_id) {
                query = database.query('DELETE FROM Inventory WHERE ItemID = ?', [_id]);
            }
    

            const inventoryItems = await query;
            if (inventoryItems.affectedRows === 0){
                return res.status(400).json({ error: "No items found" });
            }
            else {
                res.json({ status: "Success", deletedItems: inventoryItems.affectedRows });
            }

        } catch (error) {
            console.error("Error deleting item:", error);
            res.status(500).json({ error: "An error occurred while deleting the item." });
        }
    });
};
