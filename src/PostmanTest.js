pm.test("Response should be 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});

pm.test("It should return company names with Group ", function () {
    var jsonData = JSON.parse(responseBody);

    jsonData.forEach(function(element){
    if(element["company"]["name"].includes("Group")){
        console.log(element["company"]["name"])}
    });

});
