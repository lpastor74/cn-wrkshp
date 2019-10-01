import ballerina/http;
import ballerina/log;
import ballerina/io;
import ballerina/jsonutils;
import ballerinax/java.jdbc;
// import ballerina/docker;

jdbc:Client ordersDb = new({
    url: "jdbc:mysql://localhost:3306/orders?serverTimezone=UTC",
    username: "root",
    password: "root",
    poolOptions: { maximumPoolSize: 5 },
    dbOptions: { useSSL: false }
});

type Order record {
    int order_id;
    string customer_id;
    string item_code;
    string timestamp;
    float amount;
};

// @docker:Expose {}
listener http:Listener ordersEP = new(9090);

// @docker:Config {
//     name: "order_service",
//     tag: "v1"
// }

service orders on ordersEP {

    @http:ResourceConfig {
        methods: ["GET"],
        path: "/"
    }
    resource function get_all_orders(http:Caller caller, http:Request request) {
        var selectRet = ordersDb->select("SELECT * FROM orders", Order);
        string result = "No items found.";
        if (selectRet is table<Order>) {
            json jsonConversionRet = jsonutils:fromTable(selectRet);
            result = jsonConversionRet.toJsonString();
            // io:println(result);
        } else {
            error err = selectRet;
            io:println("Select data from student table failed: ",
                    <string> err.detail()["message"]);
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
    resource function get_by_id(http:Caller caller, http:Request request,int id) {
        var orderQueryResult = ordersDb->select("SELECT * FROM orders WHERE order_id=?", Order,id);
        string result = "No items found.";
        if (orderQueryResult is table<Order>) {
            json jsonConversionRet = jsonutils:fromTable(orderQueryResult);
            result = jsonConversionRet.toJsonString();
            io:println(result);
        } else {
            error err = orderQueryResult;
            io:println("Select data from student table failed: ",
                    <string> err.detail()["message"]);
        }
        var res = caller->respond(result);
        if (res is error) {
            log:printError("Error sending response", res);
        }
    }

}