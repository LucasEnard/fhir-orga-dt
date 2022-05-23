Class Python.ProductionCSV Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="Python.ProductionCSV" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="Python.ServiceCSV" Category="" ClassName="Python.ServiceCSV" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>
  <Item Name="Python.ProcessCSV" Category="" ClassName="Python.ProcessCSV" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>
  <Item Name="Python.OperationCSV" Category="" ClassName="Python.OperationCSV" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>
</Production>
}

}
