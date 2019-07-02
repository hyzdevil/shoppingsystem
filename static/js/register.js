function checkname() {
    var name = $("#username").val();
    if(name == ""){
        $("#msg1").html("用户名不能为空");
        return false;
    }else if (!isNaN(name[0])) {
        $("#msg1").html("数字不能开头");
        return false;
    }else{
        $("#msg1").html("");
        for (var i in name) {
            if (!(name[i]>='a'&&name[i]<='z')&&
                !(name[i]>='A'&&name[i]<='Z')&&
                !(name[i]>='0'&&name[i]<='9')&&!name[i]=='_') {
                $("#msg1").html("由数字、字母和下划线组成");
                return false;
            }
        }
    }
    return true;
}

function checkpass() {
    var pass = $("#userpass");
    if(pass.val() == ""){
        $("#msg2").html("密码不能为空");
        return false;
    }else{
        $("#msg2").html("");
        if(!(pass.val().length>=6&&pass.val().length<=12)) {
            $("#msg2").html("密码长度在6-12位之间");
            return false;
        }
    }
    return true;
}

function checkapass() {
    var pass = $("#userpass");
    var apass = $("#userapass");
    if(pass.val() != apass.val()){
        $("#msg3").html("密码不一致");
        return false;
    }
    $("#msg3").html("");
    return true;
}

function checkemail() {
    var email = $("#useremail")
    if (email.val() == "") {
        $("#msg4").html("邮箱不能为空");
        return false;
    } else if (email.val().indexOf("@") == -1) {
        $("#msg4").html("邮箱中没有@字符");
        return false;
    } else if (email.val().split("@").length > 2) {
        $("#msg4").html("邮箱中@字符只能出现一次");
        return false;
    } else if (email.val()[0] == "@" || email.val()[email.val().length - 1] == "@") {
        $("#msg4").html("邮箱中@字符不能出现在首尾位置");
        return false;
    } else if (email.val().substring(email.val().length - 4) != ".com" || email.val().substring(email.val().length - 5) == "@.com") {
        $("#msg4").html("请输入正确邮箱格式");
        return false;
    } else {
        $("#msg4").html("");
    }
    return true
}

function checkphone() {
    var phone = $("#userphone")
    if(phone.val() == ""){
        $("#msg5").html("电话不能为空");
        return false;
    }else{
        $("#msg5").html("");
        if(phone.val().length != 11){
            $("#msg5").html("电话号码为11位数字");
            return false;
        }else if(!(phone.val().substring(0,2) == "13" ||
            phone.val().substring(0,2) == "17" ||
            phone.val().substring(0,2) == "15" ||
            phone.val().substring(0,2) == "18" ||
            phone.val().substring(0,2) == "16")){
            $("#msg5").html("请输入正确的手机格式");
            return false;
        }
    }
    return true;
}