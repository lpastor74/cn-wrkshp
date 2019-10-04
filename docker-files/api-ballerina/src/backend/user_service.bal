import ballerina/docker;
import ballerina/http;
import ballerina/io;
import ballerina/jsonutils;
import ballerina/log;
import ballerinax/java.jdbc;

jdbc:Client usersDb = new ({
    url: "jdbc:mysql://mysql:3306/api_svc?serverTimezone=UTC",
    username: "api753",
    password: "api753_secret",
    poolOptions: {maximumPoolSize: 5},
    dbOptions: {useSSL: false}
});

@docker:Expose {}
listener http:Listener usersEP = new (9090);

type User record {
    int idUsers;
    string FirstName;
    string LastName;
    string City;
    string ZIP;
    int ExtID;
};

@docker:Config {
    name: "ballerina-cn",
    tag: "v3"
}

service users on usersEP {

    @http:ResourceConfig {
        methods: ["GET"],
        path: "/"
    }
    resource function get_all(http:Caller caller, http:Request request) {
        var selectRet = usersDb->select("SELECT * FROM users", User);
        string result = "No users found.";
        if (selectRet is table<User>) {
            json jsonConversionRet = jsonutils:fromTable(selectRet);
            result = jsonConversionRet.toJsonString();
        } else {
            error err = selectRet;
            io:println("Select data from users table failed: ",
            <string>err.detail()["message"]);
        }
        var res = caller->respond(result);
        if (res is error) {
            log:printError("Error sending response", res);
        }
    }

    @http:ResourceConfig {
        methods: ["GET"],
        path: "/{id}"
    }
    resource function get_by_id(http:Caller caller, http:Request request, int id) {
        var userQueryResult = usersDb->select("SELECT * FROM users WHERE idUsers=?", User, id);
        string result = "No items found.";
        if (userQueryResult is table<User>) {
            json jsonConversionRet = jsonutils:fromTable(userQueryResult);
            result = jsonConversionRet.toJsonString();
        } else {
            error err = userQueryResult;
            io:println("Select data from users table failed: ",
            <string>err.detail()["message"]);
        }
        var res = caller->respond(result);
        if (res is error) {
            log:printError("Error sending response", res);
        }
    }

}
