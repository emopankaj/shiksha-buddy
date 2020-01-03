<template>
    <div class="animated fadeIn">
        <b-card no-body>
            <b-card-header>
                <strong>Edit Menu</strong>
            </b-card-header>
            <b-card-body>
                <b-row class="align-items-center">
                    <b-col cols="6" sm="4" md="2" xl class="mb-3 mb-xl-0">
                        <draggable v-model="menuStructure" draggable=".item">
                            <b-button block variant="outline-primary" v-for="menuItem in menuStructure"
                                      :key="menuItem.id"
                                      class="item" @click="() => editMenuItem(menuItem.id)">
                                {{menuItem.name}}
                            </b-button>
                            <b-button slot="footer" block variant="primary" @click="addMenu">Add</b-button>

                        </draggable>
                    </b-col>
                    <b-col cols="6" sm="4" md="2" xl class="mb-3 mb-xl-0">
                        <draggable v-model="menuStructure" draggable=".item">
                            <b-button block variant="outline-primary" v-for="menuItem in menuStructure"
                                      :key="menuItem.id"
                                      class="item">
                                {{menuItem.name}}
                            </b-button>
                            <b-button slot="footer" block variant="primary">Add</b-button>

                        </draggable>
                    </b-col>
                </b-row>
            </b-card-body>
        </b-card>
        <menu-edit-form :item_id="this.current_item_id"/>
    </div>
</template>

<script>
    import draggable from 'vuedraggable'
    import MenuEditForm from "./MenuEditForm";

    export default {
        name: 'menu-edit',
        components: {
            MenuEditForm,
            draggable,
        },
        data() {
            return {
                current_item_id: '',
                menuStructure: [{
                    id: 1,
                    name: 'one',
                    type: 'intermediate_menu',
                    menus: [],
                    linked_page: {
                        id: 1,
                        page_name: ''
                    }
                }, {
                    id: 2,
                    name: 'two',
                    type: 'page_menu',
                    menus: [],
                    linked_page: {
                        id: 1,
                        page_name: ''
                    }
                }]
            };
        },
        methods: {
            addMenu() {
                this.menuStructure = [...this.menuStructure, {id: this.menuStructure.length, name: 'new item'}];
            },
            editMenuItem(item_id) {
                this.current_item_id = item_id;
            }
        }
    }
</script>
