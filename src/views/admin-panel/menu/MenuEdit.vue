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
                                      class="item" @click="() => editMenuItem(menuItem)">
                                {{menuItem.label}}
                            </b-button>
                            <b-button slot="footer" block variant="primary" @click="addMenu">Add</b-button>

                        </draggable>
                    </b-col>
                    <b-col cols="6" sm="4" md="2" xl class="mb-3 mb-xl-0">
                        <draggable v-model="menuStructure" draggable=".item">
                            <b-button block variant="outline-primary" v-for="menuItem in menuStructure"
                                      :key="menuItem.id"
                                      class="item">
                                {{menuItem.label}}
                            </b-button>
                            <b-button slot="footer" block variant="primary">Add</b-button>

                        </draggable>
                    </b-col>
                </b-row>
            </b-card-body>
        </b-card>
        <menu-edit-form :menuItem="this.currentMenuItem"/>
    </div>
</template>

<script>
    import draggable from 'vuedraggable'
    import MenuEditForm from "./MenuEditForm";
    import {EventBus} from "@/main";

    export default {
        name: 'menu-edit',
        components: {
            MenuEditForm,
            draggable,
        },
        data() {
            return {
                currentMenuItem: {},
                menuStructure: [{
                    id: 1,
                    label: 'one',
                    type: 'intermediate_menu',
                    menus: [],
                    linked_page: {
                        id: 1,
                        page_name: '',
                        pageType: ''
                    }
                }, {
                    id: 2,
                    label: 'two',
                    type: 'page_menu',
                    menus: [],
                    linked_page: {
                        id: 2,
                        page_name: '',
                        pageType: ''
                    }
                }]
            };
        },
        methods: {
            addMenu() {
                this.menuStructure = [...this.menuStructure,
                    {
                        id: this.menuStructure.length + 1,
                        label: 'Click to Edit',
                        type: 'intermediate_menu',
                        menus: [],
                        linked_page: {
                            id: 1,
                            page_name: '',
                            pageType: ''
                        }
                    }];
            },
            editMenuItem(currentMenuItem) {
                this.currentMenuItem = currentMenuItem;
            }
        },
        created() {
            EventBus.$on('update-menu-item', menuItem => {
                let updatedMenuItem = menuItem;
                let index = this.menuStructure.findIndex(menu => menu.id === updatedMenuItem.id);

                let menuStructureClone = this.menuStructure.slice();
                if (index !== -1) {
                    menuStructureClone[index] = updatedMenuItem;
                } else {
                    menuStructureClone.push(updatedMenuItem);
                }
                this.menuStructure = menuStructureClone;
            });
        }
    }
</script>
