db.createUser({
    user: "root",
    pwd: "rootteste",
    roles: [{
        role: "readWrite",
        db: "crawler"
    }]
})