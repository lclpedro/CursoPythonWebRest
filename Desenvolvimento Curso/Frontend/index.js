function initConfig($scope, $http){
    console.log('Carregamento OK!')

    let api = 'http://localhost:5000/api'

    $scope.list_contacts=[]
    
    let get_contacts = ()=>{
        $http.get(`${api}/get_contact`).then(response=>{
            $scope.list_contacts=response.data.data
        })
    }
    get_contacts()

    $scope.edit_contact=(contact)=>{
        $scope.contact = contact
        console.log(contact)
    }

    $scope.insert_contact = (contact)=>{
        console.log(contact)
        if(contact._id){
            $http.put(`${api}/update_contact/${contact._id}`, contact).then(response=>{
                get_contacts()
                $scope.contact = null
                swal({
                    title: "Muito bem!",
                    text: response.data.data,
                    icon: "success",
                    button: "Fechar",
                })
            }).catch(erro=>{
                swal(`Ops, deu algo errado ao atualizar o contato!`, {
                    icon: "error",
                })
            })
        }else{
            $http.post(`${api}/insert_contact`, contact).then(response=>{
                swal({
                    title: "Muito bem!",
                    text: response.data.data,
                    icon: "success",
                    button: "Fechar",
                });
                get_contacts();
                $scope.contact=null
            }).catch(erro=>{
                swal(`Ops, deu algo errado ao salvar o contato!`, {
                    icon: "error",
                })
            })
        }
    }

    $scope.delete_contact=(data)=>{
        console.log(data)
        $scope.name_person = data.name_person
        swal({
            title: "Você quer mesmo excluir?",
            text: `Se você confirmar, o contato de ${data.name_person} será excluido da sua lista de contatos.`,
            icon: "warning",
            buttons: ["Cancelar", "Salvar"],
            dangerMode: true,
        })
        .then((willDelete) => {
            if(willDelete){
                $http.delete(`${api}/delete_contact/${data._id}`).then(data=>{
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