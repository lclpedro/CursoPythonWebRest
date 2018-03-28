function initConfig($scope, $http){
    console.log('Carregamento OK!')
    let api = 'http://localhost:5000/api'
    let get_contacts = ()=>{
        $http.get(`${api}/contacts`).then(data=>{
            $scope.list_contacts=data.data
        })
    }
    get_contacts()

    $scope.edit_contact=(contact)=>{
     $scope.contact = contact
 }

 $scope.insert_contact = (contact)=>{
    if(contact._id){
        $http.put(`${api}/contact/${contact._id}`, contact).then(data=>{
            get_contacts()
            $scope.contact = null
            swal({
              title: "Muito bem!",
              text: data.data,
              icon: "success",
              button: "Fechar",
          })
        })
    }else{
        $http.post(`${api}/contacts`, contact).then(data=>{
            console.log(data)
            swal({
              title: "Muito bem!",
              text: data.data,
              icon: "success",
              button: "Fechar",
          });
            get_contacts();
            $scope.contact=null
        }).catch(erro=>{
            swal(`Ops, deu algo errado ao excluir o contato!`, {
                icon: "error",
            })
        })
    }
}

$scope.delete_contact=(data)=>{
    $scope.name_person = data.name_person
    swal({
        title: "Você quer mesmo excluir?",
        text: `Se você confirmar, o contato de ${data.name_person} será excluido da sua lista de contatos.`,
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
    .then((willDelete) => {
        if(willDelete){
            $http.delete(`${api}/contact/${data._id}`).then(data=>{
                get_contacts();
                swal(`Ok, Contato de ${$scope.name_person} foi deletado com Sucesso!`, {
                    icon: "success",
                });
            }).catch(erro=>{
                swal(`Ops, deu algo errado ao excluir o contato!`, {
                    icon: "error",
                })
            })
        }
    })
}

}
angular
.module('pythonWeb', [])
.controller('initConfigController', initConfig)