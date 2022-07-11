$(document).ready(function(){
    var d=new Date()
    var cat = (d.getHours())+":"+(d.getMinutes())+":"+(d.getSeconds())
    var clt = (d.getHours())+":"+(d.getMinutes())+":"+(d.getSeconds())
    var cd=(d.getFullYear())+"-"+(d.getMonth()+1)+"-"+(d.getDate())
    $('#currentdate').val(cd)
    $('#attendtime').val(cat)
    $('#leavetime').val(clt)
})