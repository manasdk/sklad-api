[ {
  type: "vms",
  label: "Virtual Machines",
  instances: [/* instance list */],
  count: "10"
  },
  { /*...*/ }
]

[ 
  {id:"vm-id1", name:"my first vm", power:"on", ip:"192.168.10.101" },
  {id:"vm-id2", name:"my first vm", power:"on", ip:"192.168.10.102" }
]

{ 
  relations: [ 
    {
      type: "vms",
      label: "Instances",
      instances: [  
        {id:"vm-id1", name:"my first vm", power:"on", ip:"192.168.10.101" },
        {id:"vm-id2", name:"my first vm", power:"on", ip:"192.168.10.102" }
      ],
      count: "2" 
    },
    { 
      type: “networks”,
      label: “Networks”,
      instances [{ id:”net-id1”, name:”my net work”, mask:”255.255.255.252” }]
    }
  ]
  properties: { 
    id: “host-id1”,
    ip: [“10.20.30.40”, “10.20.100.101”]
    /* all other propoerties */
  }
}