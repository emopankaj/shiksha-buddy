<template>
    <div class="animated fadeIn">
        <b-card no-body>
            <b-card-header>
                <strong>Edit Menu</strong>
            </b-card-header>
            <b-card-body>
                <b-row class="align-items-center">
                    <b-col cols="6" sm="4" md="2" xl class="mb-3 mb-xl-0">
                        <draggable v-model="myArray" draggable=".item">
                            <b-button block variant="outline-primary" v-for="element in myArray" :key="element.id"
                                      class="item">
                                {{element.name}}
                            </b-button>
                            <b-button slot="footer" block variant="primary">Add</b-button>

                        </draggable>
                    </b-col>
                </b-row>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
    import draggable from 'vuedraggable'

    export default {
        name: 'menu-edit',
        components: {
            draggable,
        },
        data() {
            return {myArray: [{id: 1, name: 'one'}, {id: 2, name: 'two'}]};
        }
    }
</script>
